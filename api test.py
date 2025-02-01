import requests

url = "https://autoscreenshot.onrender.com/"
response = requests.get(url)

if response.status_code == 200:
    print(response.json())  # Output the success message
else:
    print(f"Error: {response.status_code}")
