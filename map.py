#https://python-visualization.github.io/folium/quickstart.html

import folium
import pandas as pd
import numpy

m = folium.Map(
    location=[46.3014, -123.7390],
    zoom_start=7,
    tiles='Stamen Terrain'
)


folium.Marker(
    location=[47.3489, -124.708],
).add_to(m)


folium.Marker(
    location=[44.639, -124.5339],
).add_to(m)


folium.Marker(
    location=[46.216, -124.1280],
).add_to(m)

m.save('map.html')