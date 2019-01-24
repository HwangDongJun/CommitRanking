import sys
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
		for line in lines:
			user_name = line.strip()
			Ucert = git_certification(user_cert)
			cert_info = Ucert.get_info2base64()
			
			header = {'Authorization' : ('Basic ' + cert_info)}
			commit_info = repo_commit_info(header, user_name)
			repo_names = commit_info.get_repo_info()
			for repo in repo_names:
				commit_crawler = graphql_api_crawler(repo, header, user_name)
				commit_data = commit_crawler.run_query()
				pprint(commit_data)

if __name__ == '__main__':
	sys.exit(search_commit(sys.argv))
