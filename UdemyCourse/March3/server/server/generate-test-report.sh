#!/bin/bash

# Run tests and save the output to a file
cargo test -- --format=json > test_results.json

# Parse the JSON output and format it into HTML
echo "<html><body><h1>Test Report</h1><ul>" > test_report.html
cat test_results.json | jq -r '.results[] | "<li>" + .name + ": " + .result + "</li>"' >> test_report.html
echo "</ul></body></html>" >> test_report.html

# Open the HTML report in the default web browser
xdg-open test_report.html || open test_report.html

