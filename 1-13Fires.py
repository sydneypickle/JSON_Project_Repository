"""
Use the files below to compare the fires that have 
been burning in California between Sept 1-13 and 
Sept 14 - 20. This file contains information about the
latitude and longitude, and the brightness of each fire.
Using what you have learnt in processing a JSON files and
mapping, make a map that shows the fires. You will need 
separate programs to represent each JSON file. One file
is from 9-1-20 to 9-13-20 and the other is from 9-14-20
to 9-20-20. We are only interested in fires that have a
brightness factor above 450.
"""
import json
from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

infile = open("US_fires_9_1.json", "r")
fire1_data = json.load(infile)

lons, lats, brights = [], [], []

for item in fire1_data:
    lon = item["longitude"]
    lat = item["latitude"]
    bright = item["brightness"]

    if bright > 450:
        lons.append(lon)
        lats.append(lat)
        brights.append(bright)

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            "size": [0.005 * b for b in brights],
            "color": brights,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]

my_layout = Layout(title="US Fires - 9/1/2020 through 09/13/2020")

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="california_fires1.html")
