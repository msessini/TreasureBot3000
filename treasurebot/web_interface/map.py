import requests
import folium
import sys

def make_map(address, kind):
    url = "https://nominatim.openstreetmap.org/search"

    params = {
        'q': address,
        'format': 'json'
    }
    headers = {'User-Agent': "My demo geomap app"}

    response = requests.get(url, params=params, headers=headers).json()

    if response:

        latitude = response[0]['lat']
        longitude = response[0]['lon']

        overpass_url = "http://overpass-api.de/api/interpreter"

        dict_kind = {
            "Glass": "glass_bottles",
            "Clothes": "clothes",
            "Batteries": "batteries"
        }

        distance = 100
        N = 0
        while N == 0:
            if kind == "Pfand return":
                overpass_query = f"""
                [out:json];
                node
                ["amenity"="vending_machine"]
                ["vending"="bottle_return"]
                (around:{distance},{latitude},{longitude});
                out body;
                """
            else:
                overpass_query = f"""
                [out:json];
                node
                ["amenity"="recycling"]
                ["recycling:{dict_kind[kind]}"="yes"]
                (around:{distance},{latitude},{longitude});
                out body;
                """
            response = requests.get(overpass_url, params={'data': overpass_query})
            data = response.json()

            N = len(data['elements'])
            distance += 100

        zoom_start = 16
        if distance > 300:
            zoom_start = 15
        if distance > 800:
            zoom_start = 13

        m = folium.Map(location=[latitude, longitude], zoom_start=zoom_start)

        folium.Marker(
            location=[latitude, longitude],
            icon=folium.Icon(color="red", icon="home")
        ).add_to(m)

        for element in data['elements']:

            #url = "https://nominatim.openstreetmap.org/reverse"
            #params = {
            #    'lat': element['lat'],
            #    'lon': element['lon'],
            #    'format': 'json'
            #}
            #headers = {'User-Agent': "My demo geomap app"}

            #response = requests.get(url, params=params, headers=headers).json()

            folium.Marker(
                location=[element['lat'], element['lon']],
                #popup=response['address']['road'],
                icon=folium.Icon(color="green", icon="star")
            ).add_to(m)

        return m

    else:
        return None
