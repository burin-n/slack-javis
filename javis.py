import requests
import os
from slackclient import SlackClient
import time
import datetime

BOT_NAME = 'javis'

slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

while(True):
	r = requests.get('https://cueventhub.com/api')
	res = ""
	if(r.text == "hello dude"):
		#res = 'API server is in normal operation.'
		res = "If you don't see me every hr, there are some problem with server."

	else:
		res ='Sorry for inconvenient, API server is under maintainance.'
	if __name__ == "__main__":
		api_call = slack_client.api_call("chat.postMessage",
			channel="#dev_webserver",
			text=res,
			name=BOT_NAME)

		if api_call.get('ok'):
			print(str(datetime.datetime.now())+' '+res)	
			
		else:
			print("cannot connect to slack_client ")
	time.sleep(600)
