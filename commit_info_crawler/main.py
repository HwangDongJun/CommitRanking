import sys
import operator
from pprint import pprint

from get_certification import git_certification
from repo_commit import repo_commit_info
from GraphQL_crawler import graphql_api_crawler

def search_commit(argv):
	if len(argv) < 2:
		print("Type as shown : python3 main.py user_list/Uname_list.txt")
		sys.exit(0)
	with open(argv[1], 'r') as fr:
		lines = fr.readlines()
		user_cert = input("Type in the following format(userID:userPWD): ")
		ranking_user = dict()
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
				pprint(commit_data)
				
		#Choose the case with the highest number of commit attempts.
				if commit_data['data']['repository']['defaultBranchRef'] == None:
					continue
				total_count = commit_data['data']['repository']['defaultBranchRef']['target']['history']['totalCount']
				if user_name not in ranking_user:
					ranking_user[user_name] = total_count
				elif ranking_user[user_name] < total_count:
					ranking_user[user_name] = total_count
		
		sorted(ranking_user.items(), key=operator.itemgetter(1), reverse=True)
		count = 1
		for rank in ranking_user:
			print("Rank {} -> Name: {} | Count: {}".format(str(count), rank, ranking_user[rank]))
			count += 1

if __name__ == '__main__':
	sys.exit(search_commit(sys.argv))
