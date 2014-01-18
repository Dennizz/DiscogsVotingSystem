import requests

def fetch_collection(username):
	discogs_url = "http://api.discogs.com/users/" + username + "/collection/folders/0/releases?per_page=100"

	headers= {
		'User-Agent' 	: 'DiscogsVotingSystem/0.1 +http://www.ipaddr.nl',
		'From'		: 'root@ipaddr.nl',
	}

	result = {}
	resultcounter = 1

	req = requests.get(discogs_url, headers=headers)

	page = req.json()["pagination"]["page"]
	last = int(req.json()["pagination"]["urls"]["last"].split("=")[-1])

	while page != last:
		page = req.json()["pagination"]["page"]
		for release in req.json()["releases"]:
			result[resultcounter] = {
						  'artist' : release["basic_information"]["artists"][0]["name"].encode('utf-8'),
						  'title'  : release["basic_information"]["title"].encode('utf-8'),
						  'thumb'  : release["basic_information"]["thumb"],
						}
			resultcounter += 1
		if page != last:
			req = requests.get(req.json()["pagination"]["urls"]["next"], headers=headers)
	
	return result
