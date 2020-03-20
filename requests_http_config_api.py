from requests_llnw_auth import LLNWAuth
import datetime
import requests
try:import simplejson as json
except ImportError: import json

class HttpStreamingApi:
	def __init__(self, baseUrl, username, apiKey):
		self.baseUrl = baseUrl
		self.username = username
		self.apiKey = apiKey
	
	def Auth(self):
		try:
			llnw_auth = LLNWAuth(self.username, self.apiKey)
			return llnw_auth
		except:
			print ("Authentication failed. Check Username/ API/ Permissions")

	def sendHTTPRequest(self, method, uri, data):
		headers = {
			'Content-Type': 'application/json',
			'Accept': 'application/json',
		}
		response = requests.request(method, self.baseUrl+uri, auth=self.Auth(), headers=headers, data=data)
		return json.loads(response.text)

	def getSVCProfile(self, shortname):
		uri = '/svcprof/delivery/shortname/' + str(shortname)
		return self.sendHTTPRequest("GET",uri, '')

	def getSVCInstance(self, ID):
		uri = '/svcinst/delivery/' + ID
		return self.sendHTTPRequest("GET",uri, '')

	def validateSVCInstance(self, body):
		uri = '/svcinst/delivery/validate'
		return self.sendHTTPRequest("POST",uri, body)

	def createSVCInstance(self, body):
		uri = '/svcinst/delivery'
		return self.sendHTTPRequest("POST",uri, body)
		
	def updateSVCInstance(self, ID, body):
		uri = '/svcinst/delivery/' + ID
		return self.sendHTTPRequest("PUT",uri, body)
		
	def getSVCProfileConfigOption(self, shortname):
		uri = '/configoption/shortname/' + str(shortname) + '/svcProf/LLNW-Generic'
		return self.sendHTTPRequest("GET",uri, "")

	def deleteSVCInstance(self, ID):
		uri = '/svcinst/delivery/' + ID
		return self.sendHTTPRequest("DELETE", uri, "")