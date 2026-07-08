import plotly.express as px
import matplotlib.pyplot as plt
from dice import Dice

die_1 = Dice()
die_2 = Dice()
results = []

for _ in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

max_result = die_1.num_sides + die_2.num_sides

poss_results = range(2, max_result+1)
frequencies = [results.count(value) for value in poss_results]

#visualize
title = 'Rusults of rolling two d6, 1000 times'
label = {'x':'Result', 'y':'Frequeny of Result'}

fig = px.bar(x=poss_results, y=frequencies, title=title, labels=label)

#further visualization
fig.update_layout(xaxis_dtick=1)
fig.show()