import geopandas as gpd

#for the final map, we only want to find shore data for the 6 neighborhoods
#so we need to filter a geoJSON file to only include the 6 neighborhoods

# Load it in
neighborhoods = gpd.read_file('Boston_Neighborhoods.geojson')

# Filter the data for the Back Bay neighborhood
Seaport = neighborhoods[neighborhoods['Name'] == 'South Boston Waterfront']
Downtown = neighborhoods[neighborhoods['Name'] == 'Downtown']
China = neighborhoods[neighborhoods['Name'] == 'Chinatown']
Southend = neighborhoods[neighborhoods['Name'] == 'South End']
SouthBoston = neighborhoods[neighborhoods['Name'] == 'South Boston']
BeaconHill = neighborhoods[neighborhoods['Name'] == 'Beacon Hill']


# Save the filtered data as a new GeoJSON file
Seaport.to_file('seaport.geojson', driver='GeoJSON')
Downtown.to_file('downtown.geojson', driver='GeoJSON')
China.to_file('china.geojson', driver='GeoJSON')
Southend.to_file('southend.geojson', driver='GeoJSON')
SouthBoston.to_file('southboston.geojson', driver='GeoJSON')
BeaconHill.to_file('beaconhill.geojson', driver='GeoJSON')
