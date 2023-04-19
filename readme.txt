Popular Neighborhoods - Rohan Thomas

This project is a visualization of Boston's "most popular" neighborhoods, based on data collected from 20 maps from the Leventhal Map Center.

The URL used to obtain the data: "https://collections.leventhalmap.org/search/?q=Boston&format=json".

From here, I used a Kaggle notebook that we previously worked on in class, Assignment Lab Exercise: Analyzing LMEC Digital Collections Catalog and Search API. Link to the notebook here: https://www.kaggle.com/code/rohanthomas27/reading-and-scraping-lmec-metadata.

From there, I utilized the fetchSearchAPI function to obtain data on a large number of maps of the Boston area throughout the year. I used this, as the notebook allowed for very easy viewing of the JSON result using JSONDisplay.

From these results, I sifted through many of them before settling on 20 maps to use. From those 20 maps, I took out bbox data (normally an 'Envelope' object) and used the coordinates to create a polygon of the map. These polygons can be found in the heatmap.py file and are used to create the heatmap.

Essentially, the heatmap is a visualization of the most popular neighborhoods in Boston, based on the number of maps that were created of that area. A bbox generally defines the area that is mapped in the map. As such, by overlaying different bboxes on top of each other (with an opaque color that stacks), we can see the most popular areas in Boston, i.e., the places that most often appeared on maps of Boston.

The more popular an area, the darker it will be. Along with this heatmap, I have outlined the neighborhoods of Boston on a map below. Also on this map is the polygon representing the darkest area of the heatmap. From this, we can see the most popular area of Boston, along with how much of each neighborhood is contained in that square. By simple visual analysis, we can then rank the neighborhoods by most popular (Unfortunately, after hours of research, I could not find a way to automate this).

The rankings are as follows:

Seaport: as shown on the map, the Seaport neighborhood dominates almost the entire lower diagonal half of the polygon.
Downtown Crossing: The Downtown Crossing neighborhood is the second most popular and is the only other neighborhood to have a large portion of its area in the polygon, but due to its odd shape, it loses to Seaport.
Chinatown: Chinatown is the third most popular neighborhood and is the only other neighborhood to have a large portion of its area in the polygon, but as shown on the map, it is quite small compared to the other two.
South End: The South End is the fourth most popular neighborhood and only takes up a small chunk at the bottom-left corner.
South Boston: The South Boston neighborhood is the fifth most popular neighborhood and only takes up a small chunk between South End and Seaport.
Beacon Hill: The Beacon Hill neighborhood is the sixth most popular neighborhood and only takes up a very small strip at the top-left.
Now that we know which neighborhoods are the most popular, we can make some comparisons to try to find the underlying reason as to why these neighborhoods top the charts. Perhaps it is amenities, access to public transit, access to education, and more. For this project, I decided to analyze each neighborhood's distance to the coast/important ports. As we know, Boston has historically been significant in the Fishing Industry and has been a staple part of our city since its inception. As such, I wanted to see if the distance to the coast affected how popular a neighborhood was.

To do this, for each of the top 6 neighborhoods, I selected 1000 random coordinates that are within the boundaries of the neighborhood. Then, using those coordinates, I calculated the distance of the coordinate to Boston's inner Harbor, a very historically important harbor to Boston's history. Then I took the average of all 1000 distances to get the neighborhood's average distance to shore.

The results are as follows (farthest to closest):

2.34 miles - South End
2.18 miles - South Boston
1.60 miles - Beacon Hill
1.58 miles - Chinatown
1.32 miles - Seaport
1.16 miles - Downtown Crossing
Looking at these results is quite interesting. My initial hypothesis was that the ranking would be identical, the closer to the port, the higher the 'popularity'. However, this is not the case. While there seems to still be a negative correlation between distance to the port and popularity, it is not as strong as I had assumed. Thinking about it, however, this actually makes more sense. This analysis only looked at one specific quality to compare against popularity. In reality, there are thousands, if not millions of factors that go into determining how popular a neighborhood is. Things like history (how old it is), amenities, access to public transit, access to education, and many more, all have an effect on how popular a neighborhood is, as these things increase the importance of the neighborhood and bring in more people, leading to further popularity (highly populated areas are more likely to be mapped than barren areas that nobody goes to).

So to conclude, we can pretty confidently say that there does seem to be a correlation between 'popularity' and distance to integral ports (the lower the distance, the more likely to be popular). Historically speaking, this is pretty intuitive, as cities tend to center themselves around a port/harbor, and city centers will naturally be more booming economic centers. But we must also remember that correlation does not equal causation. As such, we cannot directly state that a neighborhood's popularity is caused by its distance to shore, but we can conclude that popularity and distance to shore are correlated.

Future Extensions and Suggestions:

Unfortunately, I was unable to automate the collection of bbox data, but this would be a great future extension to this project, that would allow for easy analysis of other locations.
I would also like to analyze other factors that may affect popularity, such as distance to public transit, distance to education, and more.
Additionally, my website making skills are pretty novice (this was my first completed one), so the aesthetics have room for improvement. User-friendliness and aesthetics are very important, and I would like to improve on this in the future so that people can more easily draw conclusions from the data.
Other sources:
Neighborhood Boundary data: https://bostonopendata-boston.opendata.arcgis.com/datasets/boston-neighborhoods/explore?location=42.312337%2C-71.056800%2C12.90
Photo: https://jooinn.com/boston-cityscape.html
