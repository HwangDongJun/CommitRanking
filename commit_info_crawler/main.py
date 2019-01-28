import sys
import os
import operator
import csv
import pandas as pd
from pprint import pprint

from get_certification import git_certification
from repo_commit import repo_commit_info
from GraphQL_crawler import graphql_api_crawler
from visualization import draw_chart

FILE_PATH = 'user_list/Uname_list.txt'
CSV_PATH = 'Ranking_data.csv'

def draw_data(kind, path):
	draw = draw_chart(path)
	if kind.lower() == 'bar':
		draw.bar_chart()
	else:
		draw.pie_chart()

def search_commit(argv):
	if len(argv) < 2:
		print("Type as shown : python3 main.py userID:userPWD")
		sys.exit(0)
	
	#If Ranking_data.csv exists
	check = os.path.exists("Ranking_data.csv")
	if check: #If present, fetch data for comparison with existing text files.
		csv_names = sorted(pd.read_csv('Ranking_data.csv').UserName)
		txt_names = sorted(pd.read_csv('./user_list/Uname_list.txt', names=['UserName']).UserName)
	
	# If it exists [and] the two files are not the same [or] If it does not exist
	if check and csv_names != txt_names or not check:
		with open(FILE_PATH, 'r') as fr:
			lines = fr.readlines()
			user_cert = argv[1]  # user_cert = userID:userPWD
			ranking_user = dict()
			etc_info = dict()
			for line in lines:
				user_name = line.strip()
				Ucert = git_certification(user_cert)
				cert_info = Ucert.get_info2base64()
				
				header = {'Authorization' : ('Basic ' + cert_info)} # make haeder
				commit_info = repo_commit_info(header, user_name)
				repo_names = commit_info.get_repo_info()
				
				for repo in repo_names:
					commit_crawler = graphql_api_crawler(repo, header, user_name)
					commit_data = commit_crawler.run_query()
					#pprint(commit_data) # <- If you are concerned about output information, please remove the comment.
					
			#Choose the case with the highest number of commit attempts.
					if commit_data['data']['repository']['defaultBranchRef'] == None:
						continue
					total_count = commit_data['data']['repository']['defaultBranchRef']['target']['history']['totalCount']
					etc_list = list()
					if user_name not in ranking_user:
						ranking_user[user_name] = total_count
						#etc_list => [repo_name, updatedAt]
						etc_list.append(repo)
						etc_list.append(commit_data['data']['repository']['updatedAt'])
						#etc_info => {user_name : etc_list}
						etc_info[user_name] = etc_list
					elif ranking_user[user_name] < total_count:
						ranking_user[user_name] = total_count
						etc_list.append(repo)
						etc_list.append(commit_data['data']['repository']['updatedAt'])
						etc_info[user_name] = etc_list
			
			#save csv file
			fw_data = open('Ranking_data.csv', 'w', encoding='utf-8', newline='')
			wr_data = csv.writer(fw_data)
			#sorted ranking user commit count
			ranking_user = sorted(ranking_user.items(), key=operator.itemgetter(1), reverse=True)
			count = 1
			#save csv file & print ranking user commit count
			wr_data.writerow(['UserName', 'CommitCount'])
			for rank in ranking_user:
				print("Rank {} -> UserName: {} | Count: {} | RepositoryName: {} | UpdatedAt : {}".format(str(count), rank[0], rank[1], etc_info[rank[0]][0], etc_info[rank[0]][1]))
				count += 1
				wr_data.writerow([rank[0], rank[1]])
			fw_data.close()
	
	#draw_chart (bar, pie)
	chart = input('Write the chart you want(bar or pie): ')
	draw_data(chart, CSV_PATH)

if __name__ == '__main__':
	sys.exit(search_commit(sys.argv))
