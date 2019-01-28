import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import style


class draw_chart(object):
	def __init__(self, file_path):
		self.file_path = file_path

	def bar_chart(self):
		data = pd.read_csv(self.file_path)
		#Set data to list()
		UserName = data.UserName.tolist()
		CommitCount = data.CommitCount.tolist()

		fig = plt.figure(figsize=(12, 8))
		ax = fig.add_subplot(111)
		
		ypos = np.arange(len(UserName))
		rects = plt.barh(ypos, CommitCount, align='center', height=0.5)
		plt.yticks(ypos, UserName)
		plt.xlabel(data.columns[0])
		plt.show()

	def pie_chart(self):
		style.use('ggplot')

		data = pd.read_csv(self.file_path)
		#Set data to list()
		UserName = data.UserName.tolist()
		CommitCount = data.CommitCount.tolist()
		
		fig = plt.figure(figsize=(10, 6))
		ax = fig.add_subplot(111)

		index = CommitCount.index(max(CommitCount))
		explode = list()
		for i in range(len(CommitCount)):
			if i == index:
				explode.append(0.1)
			else:
				explode.append(0.0)
		explode = tuple(explode)

		plt.pie(CommitCount, shadow=False, startangle=90, autopct='%1.0f%%', explode=explode, pctdistance=1.1)
		plt.legend(UserName, loc="best")
		plt.axis('equal')
		plt.tight_layout()
		plt.show()
