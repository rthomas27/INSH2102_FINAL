import folium
from shapely.geometry import Polygon



# map data obtained from: "https://collections.leventhalmap.org/search/?q=Boston&format=json" using the digital search API

# From the collected record, take about 20 records that contain bboxes and convert
#from envelop to a polygon feature
#number following the b, represents the year of the map
b1780 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [[
            [-71.09960734411412, 42.38778810671559],
            [-71.00079850242687, 42.38778810671559],
            [-71.00079850242687, 42.32689917916611],
            [-71.09960734411412, 42.32689917916611],
        ]]
    },
    "properties": {
        "name": "b1780"
    }
}

b1851 = {
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-71.16372563177836, 42.42206695200006],
      [-71.16372563177836, 42.29776599168536],
      [-70.95966069490545, 42.29776599168536],
      [-70.95966069490545, 42.42206695200006],
      [-71.16372563177836, 42.42206695200006]
    ]]
  }
}



b1892 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [[
            [-71.13096163917818, 42.39811387261012],
            [-71.0076858957963, 42.39811387261012],
            [-71.0076858957963, 42.30690336252926],
            [-71.13096163917818, 42.30690336252926],
            [-71.13096163917818, 42.39811387261012]
        ]]
    },
    "properties": {
        "name": "b1892"
    }
}

b1906 = {
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-71.14553970305495, 42.410149647750345],
      [-71.14553970305495, 42.30115296907567],
      [-71.00388036012947, 42.30115296907567],
      [-71.00388036012947, 42.410149647750345],
      [-71.14553970305495, 42.410149647750345]
    ]]
  }
}


b1921 = {
  "type": "Feature",
  "geometry": {
    "type": "Polygon",
    "coordinates": [[
      [-71.08766829993374, 42.36352320559607],
      [-71.00646688072719, 42.36352320559607],
      [-71.00646688072719, 42.31371247618772],
      [-71.08766829993374, 42.31371247618772],
      [-71.08766829993374, 42.36352320559607]
    ]]
  }
}

b1935 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-71.1459746182733, 42.299981150412904],
                [-71.1459746182733, 42.39255760129477],
                [-71.01581777998136, 42.39255760129477],
                [-71.01581777998136, 42.299981150412904],
                [-71.1459746182733, 42.299981150412904]
            ]
        ]
    },
    "properties": {
        "name": "b1935"
    }
}

b2017 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-71.19042715894972, 42.21617115417859],
                [-71.19042715894972, 42.39854900662373],
                [-70.98923573215176, 42.39854900662373],
                [-70.98923573215176, 42.21617115417859],
                [-71.19042715894972, 42.21617115417859]
            ]
        ]
    },
    "properties": {
        "name": "b2017"
    }
}

b1965 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-71.093, 42.376],
                [-71.093, 42.33],
                [-71.029, 42.33],
                [-71.029, 42.376],
                [-71.093, 42.376]
            ]
        ]
    },
    "properties": {
        "name": "b1965"
    }
}

b1850 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-71.07, 42.4],
                [-71.07, 42.25],
                [-70.83, 42.25],
                [-70.83, 42.4],
                [-71.07, 42.4]
            ]
        ]
    },
    "properties": {
        "name": "b1850"
    }
}

b1728 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-71.11, 42.46],
                [-71.11, 42.24],
                [-70.83, 42.24],
                [-70.83, 42.46],
                [-71.11, 42.46]
            ]
        ]
    },
    "properties": {
        "name": "b1728"
    }
}

b1901 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-71.045, 42.3975],
                [-71.045, 42.3625],
                [-70.9875, 42.3625],
                [-70.9875, 42.3975],
                [-71.045, 42.3975]
            ]
        ]
    },
    "properties": {
        "name": "b1901"
    }
}

b1910 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-71.065, 42.355],
                [-71.065, 42.32],
                [-71.01, 42.32],
                [-71.01, 42.355],
                [-71.065, 42.355]
            ]
        ]
    },
    "properties": {
        "name": "b1910"
    }
}

b1899 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-71.065, 42.355],
                [-71.065, 42.32],
                [-71.01, 42.32],
                [-71.01, 42.355],
                [-71.065, 42.355]
            ]
        ]
    },
    "properties": {
        "name": "b1899"
    }
}

b1919 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-71.065, 42.355],
                [-71.065, 42.32],
                [-71.01, 42.32],
                [-71.01, 42.355],
                [-71.065, 42.355]
            ]
        ]
    },
    "properties": {
        "name": "b1919"
    }
}

b1870 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-71.11907595745508, 42.52422057636423],
                [-71.11907595745508, 42.29041473201166],
                [-70.7295219309937, 42.29041473201166],
                [-70.7295219309937, 42.52422057636423],
                [-71.11907595745508, 42.52422057636423]
            ]
        ]
    },
    "properties": {
        "name": "b1870"
    }
}

b1886 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-71.12493670205822, 42.3870844325968],
                [-71.12493670205822, 42.29356183469436],
                [-71.0025321253918, 42.29356183469436],
                [-71.0025321253918, 42.3870844325968],
                [-71.12493670205822, 42.3870844325968]
            ]
        ]
    },
    "properties": {
        "name": "b1886"
    }
}

b2019 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-71.191, 42.397],
                [-71.191, 42.227],
                [-70.998, 42.227],
                [-70.998, 42.397],
                [-71.191, 42.397]
            ]
        ]
    },
    "properties": {
        "name": "b2019"
    }
}
b1861 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-71.10736540690698, 42.38231409674198],
                [-71.10736540690698, 42.322699206696505],
                [-71.02199254266118, 42.322699206696505],
                [-71.02199254266118, 42.38231409674198],
                [-71.10736540690698, 42.38231409674198]
            ]
        ]
    },
    "properties": {
        "name": "b1861"
    }
}

b2008 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-71.09424377279107, 42.382492119938],
                [-71.09424377279107, 42.318228259261126],
                [-71.00362484960424, 42.318228259261126],
                [-71.00362484960424, 42.382492119938],
                [-71.09424377279107, 42.382492119938]
            ]
        ]
    },
    "properties": {
        "name": "b2008"
    }
}

b1900 = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [
            [
                [-71.073, 42.369],
                [-71.073, 42.344],
                [-71.045, 42.344],
                [-71.045, 42.369],
                [-71.073, 42.369]
            ]
        ]
    },
    "properties": {
        "name": "b1900"
    }
}


#now put all of the features into a list
x = [b1780, b1851, b1892, b1906, b1921, b1935, b2017, b1965, b1850, b1728, b1901, b1910, b1899, b1919, b1870, b1886, b2019, b1861, b2008, b1900]

# Create a map object centered on the mean of the GeoJSON coordinates
m = folium.Map(location=[42.3601, -71.0589], zoom_start=10)

# Add the GeoJSON layer to the map
folium.GeoJson(b1780, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b1851, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b1892, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b1906, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b1921, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b1935, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)



folium.GeoJson(b2017, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b1965, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b1850, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b1728, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b1901, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b1910, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)



folium.GeoJson(b1899, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b1919, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b1870, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b1886, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b2019, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b1861, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)



folium.GeoJson(b2008, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)

folium.GeoJson(b1900, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 2,
        'opacity': 0.1,
    }).add_to(m)



#now we need to find te coordiantes of the darkest square, which is almost entirely udner the itnersection between b1919 and b1900

poly1 = Polygon(b1900['geometry']['coordinates'][0])
poly2 = Polygon(b1919['geometry']['coordinates'][0])

#handy tool from Shapely library
intersection = poly1.intersection(poly2)

# get the coords
intersection_coords = list(intersection.exterior.coords)

c1 = intersection_coords[0]
c2 = intersection_coords[1]
c3 = intersection_coords[2]
c4 = intersection_coords[3]
c5 = intersection_coords[4]

final_poly = {
    "type": "Feature",
    "geometry": {
        "type": "Polygon",
        "coordinates": [[
            c1,
            c2,
            c3,
            c4,
            c5
        ]]
    },
    "properties": {
        "name": "darkest_poly"
    }
}

folium.GeoJson(final_poly, style_function=lambda feature: {    
        'fillColor': '#1D4E89',           
        'color': 'black', 
        'weight': 1,
        'opacity': .7,
    }).add_to(m)

#With this, the heatmap is created and we have also the coordinates of the darkest square
#I have also outlined the darkest square for the user to see
#saving it to embed it in the website
m.save('heatmap.html')

