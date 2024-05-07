import json
import requests
from collections import OrderedDict
from flask import Flask, request, render_template
import csv

sorted_items_list = []
def search_list(find_item, list):
    for row in list:
        if row[0] == find_item:
            return row[0]
        
    return "not found"

#headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiNzQ5N2EwNWYtZWMzNi00OWU2LTg5N2QtMGIyNzAwYjI4NTVmIiwidHlwZSI6ImFwaV90b2tlbiJ9.5ek4leIgzPBElXbnKfh_uQcRpCbg0nSpEnHShHkdaMQ"}
headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoiMmQ5Y2M0ODQtZDg2Zi00NjU4LWFkNjUtNjRmNjc2NDNjOTM1IiwidHlwZSI6ImFwaV90b2tlbiJ9.-0H1AStTxPDYr_hTn5pkbJQp4zogMuh9dlYBCUoeHEw"}




api_url = "https://api.edenai.run/v2/image/object_detection"

#used to get user input from HTML
app = Flask(__name__)

@app.route('/')
def index():
    # Render the HTML form
    return render_template('index.html')

@app.route('/process', methods=['POST','GET'])
def process():
    if request.method == "POST":
        # Get the input data from the request
        file_URL = request.form["url"]
        location_label = request.form["location"]

        json_payload = {
            "providers": "amazon",
            "file_url": file_URL,
            "fallback_providers": "google"
        }

        response = requests.post(api_url, json=json_payload, headers=headers)

        with open("result.json", "w") as file:
            json.dump(json.loads(response.text), file)

        with open("result.json", "r") as file:
            data = json.load(file)

        # Print labels from each provider
            items_list = []

        for provider, provider_data in data.items():
            if provider == 'amazon':
                for item in provider_data["items"]:
                    label = item['label']
                    confidence = item['confidence']
                    location = location_label
                    items_list.append((label, confidence, location))

        # Sort the items list by label
        sorted_items_list = sorted(items_list, key=lambda x: x[0])

        print(sorted_items_list)
        return render_template('result.html', stocks = sorted_items_list)
    
    if request.method == "POST":
        render_template('result.html')

@app.route('/search', methods=['POST','GET'])
def search():
    if request.method == "POST":
        # Get the input data from the request
        item = request.form["item"]
        
        location = search_list(item, sorted_items_list)

        return render_template('search.html', location)
    if request.method == "GET":
        return render_template('search.html')
        

    # # get user input for item to be searched for
    # while True:
    #     user_input = input("Would you like to search for an item (type 'n' to exit): ")

    #     # If user enters 'n' break out of the loop
    #     if user_input.lower() == 'n':
    #         break
        
    #     item = input("Please enter item to be found: ")
    #     for label, item_data in sorted_items_list:
    #         if label == item:
    #             print("Your item is located at the", item_data['location'])
    #             break
    #     else:
    #         print("Item not found.")
        


