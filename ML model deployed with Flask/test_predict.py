# test_predict.py

import requests

# URL of your local Flask server
url = "http://127.0.0.1:5000/predict"

# Example features (similar to Iris dataset)
data = {
    "features": [5.1, 3.5, 1.4, 0.2]  # Example: Iris-setosa
}

# Send POST request
response = requests.post(url, json=data)

# Print the response
if response.status_code == 200:
    print("Prediction result:", response.json())
else:
    print("Failed to get prediction:", response.status_code)
