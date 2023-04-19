#This file will obtain distance info on each enighborhood
import geopandas as gpd
import random
from shapely.geometry import Point, LineString
from geopy.distance import great_circle
import folium
import pandas as pd

#read in each one
n1 = (gpd.read_file('seaport.geojson'))
n2 = (gpd.read_file('downtown.geojson'))
n3 = (gpd.read_file('china.geojson'))
n4 = (gpd.read_file('southend.geojson'))
n5 = (gpd.read_file('southboston.geojson'))
n6 = (gpd.read_file('beaconhill.geojson'))

#combine into one to put on map representing boundries
combined = []
combined.append(n1)
combined.append(n2)
combined.append(n3)
combined.append(n4)
combined.append(n5)
combined.append(n6)
final = gpd.GeoDataFrame(pd.concat(combined, ignore_index=True))

# turn into polygons
polygon_n1 = n1.geometry.iloc[0]
polygon_n2 = n2.geometry.iloc[0]
polygon_n3 = n3.geometry.iloc[0]
polygon_n4 = n4.geometry.iloc[0]
polygon_n5 = n5.geometry.iloc[0]
polygon_n6 = n6.geometry.iloc[0]

#now we need to find 10 random points in each polygon
def random_points_in_polygon(polygon, num_points):
    points = []
    min_x, min_y, max_x, max_y = polygon.bounds
    while len(points) < num_points:
        random_point = Point([random.uniform(min_x, max_x), random.uniform(min_y, max_y)])
        if random_point.within(polygon):
            points.append(random_point)
    return points

#we will use 1000 to get accurate results
num_points = 1000 
random_points_n1 = random_points_in_polygon(polygon_n1, num_points)
random_points_n2 = random_points_in_polygon(polygon_n2, num_points)
random_points_n3 = random_points_in_polygon(polygon_n3, num_points)
random_points_n4 = random_points_in_polygon(polygon_n4, num_points)
random_points_n5 = random_points_in_polygon(polygon_n5, num_points)
random_points_n6 = random_points_in_polygon(polygon_n6, num_points)

#now we need to find the distance between each point and the shore (using the coordinates of boston's inner harbor)
def average_distance_to_coordinates(points):
    target_point = (42.364506, -71.038887)
    distances = [great_circle((point.y, point.x), target_point).miles for point in points]
    avg_distance = sum(distances) / len(distances)
    return avg_distance

avg_distance_n1 = average_distance_to_coordinates(random_points_n1)
avg_distance_n2 = average_distance_to_coordinates(random_points_n2)
avg_distance_n3 = average_distance_to_coordinates(random_points_n3)
avg_distance_n4 = average_distance_to_coordinates(random_points_n4)
avg_distance_n5 = average_distance_to_coordinates(random_points_n5)
avg_distance_n6 = average_distance_to_coordinates(random_points_n6)

#now we can order the distances from smallest to largest
avg_distances = [
    average_distance_to_coordinates(random_points_n1),
    average_distance_to_coordinates(random_points_n2),
    average_distance_to_coordinates(random_points_n3),
    average_distance_to_coordinates(random_points_n4),
    average_distance_to_coordinates(random_points_n5),
    average_distance_to_coordinates(random_points_n6)
]

sorted_avg_distances = sorted(avg_distances, reverse=True)
print("Sorted average distances:", sorted_avg_distances)

for i, distance in enumerate(sorted_avg_distances):
    print(f"{i+1}. {distance:.2f} miles ({'n'+str(avg_distances.index(distance)+1)})")

#from here we can see that the order (closest to farthest), after repeated runs, is:
#1. Downtown
#2. Seaport
#3. China Town
#4. Beacon Hill
#5. South Boston
#6. South End

#now we can make a map with the distance lines
#for readbility, I will only add about 5 lines for each neighborhood
#just for the user to get a feel for the distance, 1000 points is too many to show on a map

# create a folium map centered at the given endpoint
map = folium.Map(location=[42.364506, -71.038887], zoom_start=10)


def add_lines_to_map(points, map):
    for point in points:
        # create a line from the current point to the target point
        line = folium.PolyLine(locations=[(point.y, point.x), (42.364506, -71.038887)], color='red')
        # add the line to the map
        line.add_to(map)
        folium.CircleMarker(location=[point.y, point.x], radius=5, color='blue', fill=True, fill_color='blue').add_to(map)

#need to reset value of num_points, I can assure you that 1000 points is too many to show on a map lol
num_points = 5
add_lines_to_map(random_points_in_polygon(polygon_n1, num_points), map)
add_lines_to_map(random_points_in_polygon(polygon_n2, num_points), map)
add_lines_to_map(random_points_in_polygon(polygon_n3, num_points), map)
add_lines_to_map(random_points_in_polygon(polygon_n4, num_points), map)
add_lines_to_map(random_points_in_polygon(polygon_n5, num_points), map)
add_lines_to_map(random_points_in_polygon(polygon_n6, num_points), map)


#add borders
folium.GeoJson(final).add_to(map)
# display the map
map.save('6map.html')

