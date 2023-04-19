#creates and saves a map with the neighborhoods of Boston outlined and saves it
#to embedd in website

#also highlgihts darkest polygon


import folium
import json

with open('Boston_Neighborhoods.geojson') as f:
    data = json.load(f)

m = folium.Map(location=[42.3601, -71.0589], zoom_start=12)
folium.GeoJson(data).add_to(m)

final_poly = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [[
            [-71.045, 42.344],
            [-71.065, 42.344],
            [-71.065, 42.355],
            [-71.045, 42.355],
            [-71.045, 42.344]
        ]]
    },
    "properties": {
        "name": "darkest_poly"
    }
}

folium.GeoJson(final_poly, style_function=lambda feature: {    
        'fillColor': '#B7CE42',           
        'color': 'black', 
        'weight': 1,
        'opacity': .7,
    }).add_to(m)

m.save('boston_neighborhoods_map.html')


