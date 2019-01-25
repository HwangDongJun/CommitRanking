import json
import csv
import urllib
import urllib.request

USER_EVENT = 'https://api.github.com/users/{id}/events'


class git_events(object):
	def __init__(self, name, cert):
		self.name = name
		self.cert = cert

	def get_event(self):
		HEADER = { 'Authorization' : ('Basic ' + self.cert) }
		request_dict = {'id': self.name}
		event_cert = urllib.request.Request(USER_EVENT.format_map(request_dict), headers = HEADER)
		ur = urllib.request.urlopen(event_cert)
		raw_data = ur.read()
		encoding = ur.info().get_content_charset('utf-8')
		events = json.loads(raw_data.decode(encoding))
		
		#The process of outputting the type and number of events of a user
		edict = dict()
		for event in events:
			e = event['type']
			if e in edict:
				edict[e] += 1
			else:
				edict[e] = 1

		print(edict)
		
		fw = open('Events_data.csv', 'w', encoding='utf-8', newline='')
		wr = csv.writer(fw)
		wr.writerow(['EventName', 'EventCount'])
		for data in edict:
			wr.writerow([data, edict[data]])
		fw.close()
		print("-----Completed csv file creation-----")
