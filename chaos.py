import json
import requests
from collections import OrderedDict
from flask import Flask, request, render_template

headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzQ5N2EwNWYtZWMzNi00OWU2LTg5N2QtMGIyNzAwYjI4NTVmIiwidHlwZSI6ImFwaV90b2tlbiJ9.5ek4leIgzPBElXbnKfh_uQcRpCbg0nSpEnHShHkdaMQ"}

# # Get input from user - continues until user inputs 'n' to adding more photos
# while True:
#     user_input = input("Would you like to add a photo (type 'n' to exit): ")

#     # If user enters 'n' break out of the loop
#     if user_input.lower() == 'n':
#         break
    
#     file_URL = input("Please enter photo URL: ")
#     location = input("Please enter the location of the photo: ")


api_url = "https://api.edenai.run/v2/image/object_detection"

#used to get user input from HTML
app = Flask(__name__)

@app.route('/')
def index():
    # Render the HTML form
    return app.send_static_file('index.html')

@app.route('/index', methods=['POST'])
def process():
    if request.method == "POST":
        # Get the input data from the request
        file_URL = request.form.get["url"]
        location_label = request.json["location"]

        json_payload = {
            "providers": "google,amazon",
            # Messy Desk
            "file_url": file_URL,
            "fallback_providers": ""
        }

        response = requests.post(api_url, json=json_payload, headers=headers)

        with open("result.json", "w") as file:
            json.dump(json.loads(response.text), file)

        with open("result.json", "r") as file:
            data = json.load(file)

        # Print labels from each provider
        items_dict = OrderedDict()
        for provider, provider_data in data.items():
            #print(f"Labels from {provider}:")

            if provider == 'amazon':
                for item in provider_data["items"]:
                    items_dict[item['label']] = {'confidence': item['confidence'], 'location': location_label}
                    #print(item['label'], items_dict[item['label']])

        sorted_items_dict = OrderedDict(sorted(items_dict.items()))

        return render_template("result.html", stocks=sorted_items_dict)

        #for label, item_data in sorted_items_dict.items():
            #print(label, item_data)

    #if request.method == "GET":
        #return render_template("index.html", stocks=sorted_items_dict)
    # get user input for item to be searched for
    # while True:
    #     user_input = input("Would you like to search for an item (type 'n' to exit): ")

    #     # If user enters 'n' break out of the loop
    #     if user_input.lower() == 'n':
    #         break
        
    #     item = input("Please enter item to be found: ")
    #     for label, item_data in sorted_items_dict.items():
    #         if label == item:
    #             print("Your item is located at the", item_data['location'])
    #             break
    #     else:
    #         print("Item not found.")
        


