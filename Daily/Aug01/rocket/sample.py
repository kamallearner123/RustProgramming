import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import time
import json

# === Configuration ===
CSV_FILE = "junos.csv"
DESCRIPTION_COL = "Scope-Product-Group"
PR_ID_COL = "number"
OUTPUT_FILE = "missing_versions.txt"
REF_URL = "https://gnats.juniper.net/web/default/PRIDNUM"  # Removed #scope_tab
LOGIN_URL = "https://gnats.juniper.net/web/default/login"  # Replace with actual login URL
USERNAME = "your_username"  # Replace with your username
PASSWORD = "your_password"  # Replace with your password
OS_NAME = "junos"
Version = ["23.2R2", "23.4R2", "24.2R2", "24.4R2", "25.2R1", "25.2R2"]

# === Read CSV file ===
if not os.path.exists(CSV_FILE):
    print(f"File {CSV_FILE} does not exist. Please check the file path.")
    exit(1)
df = pd.read_csv(CSV_FILE)
if df.empty:
    print(f"The file {CSV_FILE} is empty. Please check the file content.")
    exit(1)

# === Setup Requests Session ===
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Referer': LOGIN_URL,
    'Upgrade-Insecure-Requests': '1',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document'
})

# === Login Function ===
def attempt_login():
    try:
        print(f"Fetching login page: {LOGIN_URL}")
        login_page = session.get(LOGIN_URL, timeout=10)
        login_page.raise_for_status()
        
        # Extract all form fields
        soup = BeautifulSoup(login_page.text, 'html.parser')
        form = soup.find('form')
        if not form:
            print("Error: No login form found on page")
            return False
        
        payload = {
            'username': USERNAME,  # Update to actual form field name
            'password': PASSWORD   # Update to actual form field name
        }
        for input_tag in form.find_all('input'):
            name = input_tag.get('name')
            value = input_tag.get('value', '')
            if name and name not in ['username', 'password']:
                payload[name] = value
        print(f"Form fields: { {k: v for k, v in payload.items() if k != 'password'} }")

        # Send login credentials
        print(f"Attempting login to: {LOGIN_URL}")
        response = session.post(LOGIN_URL, data=payload, timeout=10, allow_redirects=True)
        response.raise_for_status()

        # Print cookies and redirect chain
        cookies = session.cookies.get_dict()
        print(f"Session cookies after login: {cookies}")
        if response.history:
            print("Login redirect chain:")
            for r in response.history:
                print(f"  {r.status_code}: {r.url} -> {r.headers.get('Location', 'No Location header')}")

        # Check for login success
        if "Welcome" in response.text or (response.status_code == 200 and "login" not in response.url.lower()):
            print(f"Login successful. Final URL: {response.url}")
            return True
        else:
            print("Login failed: Response indicates login page or error")
            print(f"Response URL: {response.url}")
            print(f"Response text: {response.text[:500]}...")
            return False

    except requests.exceptions.RequestException as e:
        print(f"Login error: {str(e)}")
        if "connection" in str(e).lower():
            print("Check network connectivity, VPN, or DNS resolution for gnats.juniper.net")
        return False

# === Initial Login ===
if not attempt_login():
    print("Initial login failed. Exiting.")
    exit(1)

# === Function to Check Missing Versions ===
def Get_Missing_Versions(junos_df, Versions):
    missing_versions = []
    Traversed_PRs = []

    for index, row in junos_df.iterrows():
        pr_id = row[PR_ID_COL]
        if pd.isna(pr_id) or pr_id in Traversed_PRs:
            print(f"Skipping row {index} with PR-ID: {pr_id} (NaN or already traversed)")
            continue

        url = REF_URL.replace("PRIDNUM", str(pr_id))
        Traversed_PRs.append(str(pr_id))

        # Re-login before each PR-ID request
        print(f"Re-logging in for PR-ID: {pr_id}")
        if not attempt_login():
            missing_versions.append(f"PR-ID: {pr_id}, Re-login failed")
            continue

        try:
            print(f"Accessing URL: {url}")
            session.headers.update({'Referer': LOGIN_URL})
            response = session.get(url, timeout=10, allow_redirects=True)
            response.raise_for_status()

            # Log redirect chain
            if response.history:
                print(f"Redirect chain for {url}:")
                for r in response.history:
                    print(f"  {r.status_code}: {r.url} -> {r.headers.get('Location', 'No Location header')}")

            # Check for redirect to login page
            if "login" in response.url.lower() or "login" in response.text.lower():
                missing_versions.append(f"PR-ID: {pr_id}, Redirected to login page. Session may have expired.")
                print(f"Redirect detected. Final URL: {response.url}")
                print(f"Response text: {response.text[:200]}...")
                continue

            # Debugging: Print response details
            print(f"Final URL: {response.url}")
            print(f"Response status: {response.status_code}")
            print(f"Response headers: {json.dumps(dict(response.headers), indent=2)}")
            print(f"Response text snippet: {response.text[:200]}...")

            # Check for JavaScript dependency
            if "<script" in response.text.lower() and not any(version.lower() in response.text.lower() for version in Versions):
                print(f"Warning: Page for PR-ID {pr_id} may require JavaScript rendering")
                missing_versions.append(f"PR-ID: {pr_id}, Page may require JavaScript")

            # Parse with BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            page_text = soup.get_text().lower()
            print(f"page_text snippet: {page_text[:200]}...")

            # Check for versions
            found_versions = [version.lower() for version in Versions if version.lower() in page_text]
            if len(found_versions) != len(Versions):
                missing = [version for version in Versions if version.lower() not in found_versions]
                missing_versions.append(f"PR-ID: {pr_id}, Missing Versions: {', '.join(missing)}")
                print(f"PR-ID: {pr_id} is missing versions: {', '.join(missing)}")
            else:
                print(f"PR-ID: {pr_id} has all required versions: {', '.join(found_versions)}")

        except requests.exceptions.ConnectionError as e:
            missing_versions.append(f"PR-ID: {pr_id}, Could not reach host: {str(e)}")
            print("Check network connectivity, VPN, or DNS resolution.")
        except requests.exceptions.RequestException as e:
            missing_versions.append(f"PR-ID: {pr_id}, Error accessing URL: {str(e)}")
            if response:
                print(f"Error response URL: {response.url}")
                print(f"Error response text: {response.text[:200]}...")

        time.sleep(1)  # Prevent rate-limiting

    if missing_versions:
        print("PR-IDs with missing versions or errors:")
        for result in missing_versions:
            print(result)
        with open(OUTPUT_FILE, 'w') as f:
            f.write("PR-IDs with Missing Versions or Errors:\n")
            f.write('\n'.join(missing_versions))
        print(f"\nResults saved to {OUTPUT_FILE}")
    else:
        print("All PR-IDs have all required versions.")

# === Filter and Process ===
junos_df = df[df[DESCRIPTION_COL].str.contains('junos', case=False, na=False)]

if junos_df.empty:
    print(f"No rows found with '{DESCRIPTION_COL}' containing 'junos'.")
else:
    print(f"Found {len(junos_df)} rows with '{DESCRIPTION_COL}' containing 'junos'.")
    Get_Missing_Versions(junos_df, Version)