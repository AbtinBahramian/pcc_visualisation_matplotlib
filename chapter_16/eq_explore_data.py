from pathlib import Path
import plotly.express as px
import json

with open('eq_data/eq_all_month_June.geojson', encoding="utf-8") as f:
   my_object = json.load(f)
# path = Path('eq_data/eq_data_7_day_m1.geojson', encoding="utf-8")
# contents = path.read_text()
# all_eq_data = json.loads(my_object)

#creating a more readable version of the data
# path = Path('eq_data/readable_eq_data.txt')
# readable_content = json.dumps(my_object, indent=4)
# path.write_text(readable_content)

all_eq_dict = my_object['features']
fig_title = my_object['metadata']['title']
mags, lons, lats, titles = [], [], [], []

for eq_dict in all_eq_dict:
   try:
      mag = eq_dict['properties']['mag']
      longtitude = eq_dict['geometry']['coordinates'][0]
      latitude = eq_dict['geometry']['coordinates'][1]
      title = eq_dict['properties']['title']
   except:
      pass
   else:
      lons.append(longtitude)
      lats.append(latitude)
      titles.append(title)
      mags.append(mag)

# these are for a situation where we had negative and none value for size which makes error
abs_mags = []
for x in mags:
   if x and x > 0:
      abs_mags.append(abs(x))
   else:
      abs_mags.append(0)

#visualization
fig = px.scatter_geo(lat = lats, lon = lons, size=abs_mags ,title=fig_title,
                     color=mags,
                     color_continuous_scale='Viridis',
                     labels={'color': 'Magnitude'},
                     projection='natural earth',
                     hover_name=titles)
fig.show()