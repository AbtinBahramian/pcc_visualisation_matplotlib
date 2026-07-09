from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
import csv

path_sitka = Path('weather_data/sitka_weather_2021_full.csv')
path_death = Path('weather_data/death_valley_2021_full.csv')

lines2 = path_death.read_text().splitlines()
reader2 = csv.reader(lines2)
header2 = next(reader2)

lines1 = path_sitka.read_text().splitlines()
reader1 = csv.reader(lines1)
header1 = next(reader1)

# for index, x in enumerate(header2):
#      print(index, x)

# for sitka
PRCP, current_date = [], []
for row in reader1:
    date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        p = float(row[5])
    except ValueError:
        print(f"Wrong data in {current_date}")
    else:
        PRCP.append(p)
        current_date.append(date)

# for death valley
prcp, current_date2 = [], []
for row in reader2:
    date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        p = float(row[3])
    except ValueError:
        print(f"Wrong data in {current_date2}")
    else:
        prcp.append(p)
        current_date2.append(date)

#visualize
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(current_date, PRCP, color='blue')
ax.plot(current_date2, prcp, color='red')

fig.autofmt_xdate()

plt.show()
