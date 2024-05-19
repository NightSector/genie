import json
import requests
import sys
# Replace with your actual Google Cloud API key (avoid exposing it publicly)
API_KEY = "AIzaSyDDMCsH6YTQEA1ZHwBTPPrnAjbqY9rqOJo"
text = ""

if len(sys.argv) > 1:



    text = sys.argv[1]

# Define the URL and prompt
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + API_KEY
prompt = {"contents": [{"parts": [{"text":"only answer questions about bash else sorry i can't answer this question "+text}]}]}

# Set headers and data
headers = {'Content-Type': 'application/json'}
data = json.dumps(prompt)

try:
    # Send POST request with error handling
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()  # Raise an exception for non-200 status codes

    # Get the generated text from the successful response
    generated_text = response.json().get('candidates')[0].get('content').get('parts')[0].get('text')

    # Print the generated text
    print(generated_text)

except requests.exceptions.RequestException as e:
    print(f"An error occurred while communicating with the API: {e}")
