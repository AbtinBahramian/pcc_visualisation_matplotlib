import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(50_000)
rw.fill_walk()
point_num = range(rw.num_points) # to start less color and be more colorful at the end

plt.style.use('bmh')
fig, ax = plt.subplots(figsize=(16,9))
ax.scatter(rw.x_values, rw.y_values, c=point_num, cmap="Blues", edgecolors='none', s=1)
#ax.plot(rw.x_values, rw.y_values, linewidth=1)
#first node
ax.scatter(0,0,c='green',s=100)
#last point
ax.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=100)
ax.set_aspect("equal")

#removing axes
ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

ax.set_title("Random Walk", fontsize=24)
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("Y", fontsize=14)

ax.tick_params(labelsize = 14)

plt.show()