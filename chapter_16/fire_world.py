from pathlib import Path
import plotly.express as px
import csv

path = Path('fire_data/world_fires_7_day.csv')
contents = path.read_text().splitlines()
reader = csv.reader(contents)
header = next(reader)

for index, x in enumerate(header):
    print(index, x)

lats, longs, brightness = [], [], []
for row in reader:
    lats.append(float(row[0]))
    longs.append(float(row[1]))
    brightness.append(float(row[2]))

#visualization
fig = px.scatter_geo(lat=lats, lon=longs, title='Fires in 7 days ago',
                     size=brightness,
                     color=brightness,
                     color_continuous_scale='Viridis',
                     labels={'color':'Brightness'},
                     projection='natural earth')
fig.show()