from pathlib import Path
import geopandas as gpd
import json

with open('eq_data/eq_data_1_day_m1.geojson', encoding="utf-8") as f:
   my_object = json.load(f)
# path = Path('eq_data/eq_data_7_day_m1.geojson', encoding="utf-8")
# contents = path.read_text()
# all_eq_data = json.loads(my_object)

#creating a more readable version of the data
path = Path('eq_data/readable_eq_data.txt')
readable_content = json.dumps(my_object, indent=4)
path.write_text(readable_content)
