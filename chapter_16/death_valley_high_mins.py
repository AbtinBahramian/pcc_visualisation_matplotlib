from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
import csv

path = Path('weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, colomn_header in enumerate(header_row):
    print(index, colomn_header)

#extracting high,min Temps and dates
highs, mins, dates = [], [], []
for row in reader:
    date = datetime.strptime(row[2], "%Y-%m-%d")
    try:
        high = int(row[3])
        min = int(row[4])
    except ValueError:
        print(f'Invalid data in {date}')
    else:
        highs.append(high)
        mins.append(min)
        dates.append(date)

#visualization
plt.style.use('classic')
fig,ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, mins, color='blue', alpha=0.5)
ax.fill_between(dates, highs, mins, facecolor='blue', alpha=0.1)

plt.title('Daily Low and High Temprature, Death Valley, 2021', fontsize=24)
plt.xlabel('Dates', fontsize=14)
plt.ylabel('Temprature(F)', fontsize=14)
plt.tick_params(labelsize=14)
fig.autofmt_xdate() # to show the dates diagnaly

plt.show()