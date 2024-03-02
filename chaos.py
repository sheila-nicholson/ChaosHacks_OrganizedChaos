import json
import requests

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzQ5N2EwNWYtZWMzNi00OWU2LTg5N2QtMGIyNzAwYjI4NTVmIiwidHlwZSI6ImFwaV90b2tlbiJ9.5ek4leIgzPBElXbnKfh_uQcRpCbg0nSpEnHShHkdaMQ"}

url = "https://api.edenai.run/v2/image/object_detection"
json_payload = {
    "providers": "google,amazon",
    # Messy Desk
    "file_url": "https://media-cldnry.s-nbcnews.com/image/upload/t_fit-760w,f_auto,q_auto:best/newscms/2019_02/2706861/190107-messy-desk-stock-cs-910a.jpg",
    "fallback_providers": ""
}

response = requests.post(url, json=json_payload, headers=headers)

with open("result.json", "w") as file:
    json.dump(json.loads(response.text), file)

with open("result.json", "r") as file:
    data = json.load(file)

# Print labels from each provider
items_dict = {}
for provider, provider_data in data.items():
    #print(f"Labels from {provider}:")
    for item in provider_data["items"]:
        #print(item["label"])
        items_dict[item['label'] = item['confidence'] 
    
print(items_dict)