import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzQ5N2EwNWYtZWMzNi00OWU2LTg5N2QtMGIyNzAwYjI4NTVmIiwidHlwZSI6ImFwaV90b2tlbiJ9.5ek4leIgzPBElXbnKfh_uQcRpCbg0nSpEnHShHkdaMQ"}

url = "https://api.edenai.run/v2/image/object_detection"
json_payload = {
    "providers": "google,amazon",
    "file_url": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.msnbc.com%2Fknow-your-value%2Fwhy-cluttered-desk-kills-your-productivity-how-fix-it-n956316&psig=AOvVaw21nrBIpSmw6AH0wtiTrrUP&ust=1709485640703000&source=images&cd=vfe&opi=89978449&ved=0CBMQjRxqFwoTCMDbubOI1oQDFQAAAAAdAAAAABAE",
    "fallback_providers": ""
}

response = requests.post(url, json=json_payload, headers=headers)

result = json.loads(response.text)
print(result["google"]["items"])
