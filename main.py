from fastapi import FastAPI, Query
import requests

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    return{'Hello': 'World'}

@app.get('/api/restaurants/')
def get_restaurants(restaurant: str = Query(None)):
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'
    response = requests.get(url)
    if response.status_code == 200:
        data_json = response.json()
        if restaurant is None:
            return {'data': data_json}
        data_restaurants = []
        for i in data_json:
            if i['Company'] == restaurant:
                data_restaurants.append({
                    'item': i['Item'],
                    'price': i['price'],
                    'description': i['description']
                    })
        return {'Resturant': restaurant, 'Menu': data_restaurants}
    else:
        return{'Error': f'{response.status_code} - {response.text}...'}
