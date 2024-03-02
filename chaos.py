import json
import requests
from collections import OrderedDict

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzQ5N2EwNWYtZWMzNi00OWU2LTg5N2QtMGIyNzAwYjI4NTVmIiwidHlwZSI6ImFwaV90b2tlbiJ9.5ek4leIgzPBElXbnKfh_uQcRpCbg0nSpEnHShHkdaMQ"}

# Get input from user - continues until user inputs 'n' to adding more photos
while True:
    user_input = input("Would you like to add a photo (type 'n' to exit): ")

    # If user enters 'n' break out of the loop
    if user_input.lower() == 'n':
        break
    
    file_URL = input("Please enter photo URL: ")
    location = input("Please enter the location of the photo: ")


url = "https://api.edenai.run/v2/image/object_detection"
json_payload = {
    "providers": "google,amazon",
    # Messy Desk
    "file_url": file_URL,
    "fallback_providers": ""
}

response = requests.post(url, json=json_payload, headers=headers)

with open("result.json", "w") as file:
    json.dump(json.loads(response.text), file)

with open("result.json", "r") as file:
    data = json.load(file)

# Print labels from each provider
location_label = "Desk"
items_dict = OrderedDict()
for provider, provider_data in data.items():
    #print(f"Labels from {provider}:")

    if provider == 'amazon':
        for item in provider_data["items"]:
            items_dict[item['label']] = {'confidence': item['confidence'], 'location': location_label}
            #print(item['label'], items_dict[item['label']])

sorted_items_dict = OrderedDict(sorted(items_dict.items()))

for label, item_data in sorted_items_dict.items():
    print(label, item_data)

# get user input for item to be searched for
while True:
    user_input = input("Would you like to search for an item (type 'n' to exit): ")

    # If user enters 'n' break out of the loop
    if user_input.lower() == 'n':
        break
    
    item = input("Please enter item to be found: ")
    
print(items_dict)

