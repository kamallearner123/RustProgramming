#[tauri::command]
async fn get_greeting() -> Result<String, String> {
    let response = reqwest::get("http://127.0.0.1:8000/api/greet/")
        .await
        .map_err(|e| e.to_string())?;

    let json: serde_json::Value = response.json().await.map_err(|e| e.to_string())?;
    Ok(json["message"].to_string())
}

