import sys

from get_certification import git_certification
from repo_commit import repo_commit_info

def search_commit(argv):
	if len(argv) < 2:
		print("Type as shown : python3 main.py user_list/Uname_list.txt")
		sys.exit(0)
	with open(argv[1], 'r') as fr:
		lines = fr.readlines()
		for line in lines:
			user_name = line.strip()
			Ucert = git_certification(user_name)
			cert_info = Ucert.get_info2base64()
			
			header = {'Authorization' : ('Basic ' + cert_info)}
			commit_info = repo_commit_info(header, user_name)
			repo_names = commit_info.get_repo_info()
			for repo in repo_names:
				commit_info.get_commit_info(repo)

if __name__ == '__main__':
	sys.exit(search_commit(sys.argv))
