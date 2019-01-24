import base64
import json
import urllib
import urllib.request


class git_certification(object):
	def __init__(self, Uinfo):
		self.user_info = Uinfo
		#self.b64_info = self.get_info2base64
		#self.opener = None

	def get_info2base64(self):
		cert = self.user_info
		cert = cert.encode('utf-8')
		cert = base64.b64encode(cert)
		cert = cert.decode('utf-8')
		return cert
	'''
	def get_opener(self):
		if self.opener is not None:
			return self.opener
		self.opener = urllib.request.build_opener()
		self.opener.addheaders = [('Authorization', 'Basic ' + str(self.b64_info))]
		return self.opener
	'''
