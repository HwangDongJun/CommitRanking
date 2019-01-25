import sys
import pandas as pd
import numpy as np
from math import pi
import matplotlib.pyplot as plt

#Set data
events = pd.read_csv('Events_data.csv')
EventName = events.EventName.tolist()
EventCount = events.EventCount.tolist()

N = len(EventName)

#Find the circumference of the circle for each range.
x_as = [n/float(N) * 2 * pi for n in range(N)]

#Because the chart needs to be round, add the first part at the end of the list
# ex) a b c d a
EventCount += EventCount[:1]
x_as += x_as[:1]

#Set color of axes
plt.rc('axes', linewidth=0.5, edgecolor='#888888')

#Set polar plot
#111 describes the location of the subplot in rows, columns, and index
ax = plt.subplot(111, polar=True)

#Set clockwise rotation
#Sets the offset of the position of 0 in radians
ax.set_theta_offset(pi/2)
#Increase direction of theta (-1 increases clockwise)
ax.set_theta_direction(-1)

#Set position of y-labels
ax.set_rlabel_position(0)

#Set color and linestyle of grid
ax.xaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)
ax.yaxis.grid(True, color="#888888", linestyle='solid', linewidth=0.5)

#Set number of radial axes and remove labels
plt.xticks(x_as[:-1], [])

#Set yticks
max_count = max(EventCount) * 2
scope = np.linspace(max_count/5, max_count, 5).tolist()
plt.yticks(scope, map(str, map(int, scope))) #plt.yticks(type->int list, type-> string list)

#Plot data
ax.plot(x_as, EventCount, linewidth=0, linestyle='solid', zorder=3)

#Fill area
#b is blue, alpha is transparency
ax.fill(x_as, EventCount, 'b', alpha=0.3)

#Set axes limits
plt.ylim(0, max_count)

#Draw ytick labels to make sure they fit properly
for i in range(N):
	angle_rad = i / float(N) * 2 * pi

	if angle_rad == 0:
		ha, distance_ax = "center", 2
	elif 0 < angle_rad < pi:
		ha, distance_ax = "left", 1
	elif angle_rad == pi:
		ha, distance_ax = "center", 2
	else:
		ha, distance_ax = "right", 1
	
	ax.text(angle_rad, max_count + distance_ax, EventName[i], size=10, horizontalalignment=ha, verticalalignment="center")

#Show polar plot
plt.show()
