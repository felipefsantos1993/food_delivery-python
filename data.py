import requests
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
response = requests.get(url)

if response.status_code == 200:
    data_json = response.json()
    data_restaurants = {}
    for i in data_json:
        restaurant_name = i['Company']
        if restaurant_name not in data_restaurants:
            data_restaurants[restaurant_name] = []
        data_restaurants[restaurant_name].append({
            'item': i['Item'],
            'price': i['price'],
            'description': i['description']
            })
else:
    print(f'Error {response.status_code}')

for restaurant_name, data in data_restaurants.items():
    file_name = f'{restaurant_name}.json'
    with open(file_name, 'w') as restaurant_file:
        json.dump(data, restaurant_file)