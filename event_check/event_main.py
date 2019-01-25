import csv
import sys
import subprocess

from get_certification import git_certification
from repo_get_event import git_events

def search_user_event(argv):
	if len(argv) < 2:
		print("Type as shown : python3 main.py userID:userPWD")
		sys.exit(0) #exit system
	
	#name = get_username(git) #get_username(git)
	name = input('input name : ')
	github_cert = git_certification(argv[1])
	bs64_info = github_cert.get_info2base64() #ID:PWD -> encoding base64
	
	#Displays the type and number of events of the user
	eve = git_events(name, bs64_info)
	eve.get_event()

	#Draw radar chart
	subprocess.call("python3 event_radar_chart.py " + name, shell=True) 

if __name__ == '__main__':
	sys.exit(search_user_event(sys.argv))
