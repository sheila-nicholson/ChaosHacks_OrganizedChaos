import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzQ5N2EwNWYtZWMzNi00OWU2LTg5N2QtMGIyNzAwYjI4NTVmIiwidHlwZSI6ImFwaV90b2tlbiJ9.5ek4leIgzPBElXbnKfh_uQcRpCbg0nSpEnHShHkdaMQ"}

url = "https://api.edenai.run/v2/image/object_detection"
json_payload = {
    "providers": "google,amazon",
    "file_url": "https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/newscms/2019_02/2706861/190107-messy-desk-stock-cs-910a.jpg",
    "fallback_providers": ""
}

response = requests.post(url, json=json_payload, headers=headers)

result = json.loads(response.text)
print(result["amazon"]["items"])
