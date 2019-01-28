# CommitRanking

### Rank the number of commits in the github repository of the specified user.

1. Using Interface
	- Rest API
	- GraphQL API

2. Using Language
	- Python 3.5.2

3. Reference site
	- https://developer.github.com/v3/     [Rest API]
	- https://developer.github.com/v4/     [GraphQL API]

4. How to use (commit_info_crawler)
	- Fill in the user_list/Uname_list file with the name of the person you want to search for, one per line.
	- python3 main.py userID:userPWD  <-- Run command

5. Output Type
	- Rank [count] -> UserName: [UserName] | Count: [CommitCount] | RepositoryName: [RepositoryName] | UpdatedAt: [LastUpdatedTime]

6. Result Data
![result_img](./img_file/result_img.PNG)

7. Draw Bar/Pie Chart
- Change Input Format <br>
![input_format](./img_file/input_chart.PNG)

- Bar Chart <br>
![draw_chart_img](./img_file/draw_chart_img.PNG)

- Pie Chart <br>
![draw_pie_chart](./img_file/draw_pie_chart.PNG)
<br>
**Due to the large differences between the data, the pie chart showed 0% in part. Some modifications have been made.**

---
## Github User EventData

#### Navigate to your events independently of the RankingCommit.

1. How to use (event_check)
	- python3 event_main.py userID:userPWD <-- Run command
	- input name: [Here!] -> Enter the name of the user you want to crawl!!!

2. Result Data

![result_event_img](./img_file/event_result_img.PNG)

3. Draw Radar Chart
	- The position of the value displayed in the radar chart is random
![draw_radar_chart](./img_file/draw_radar_chart.PNG)

#### The data for output is a random user in Github.
