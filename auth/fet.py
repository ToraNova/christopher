# fet_itp.py library
# contains auxiliary functions to authenticate a session with a valid password
# depends on requests and HTMLparser libs

import requests
from html.parser import HTMLParser

class TokenParse(HTMLParser):
	static_ref = ('name','MyToken')
	tokenVal = None

	def handle_starttag(self,tag,attrs):
		if(tag=="input"):
			if self.static_ref in attrs:
				self.tokenVal = attrs[2][1]
		else:
			pass
	def handle_endtag(self,tag):
		pass
	def handle_data(self,data):
		pass

def login(sid,passw):

	pars = TokenParse()

	#attack_session
	sess = requests.Session()

	#login process
	login_req = sess.get('http://fet.mmu.edu.my/itp/index_files/public_index.php?logout=1&action=student_login')
	pars.feed(login_req.text)
	#print("[FET_ITP]Token val :",pars.tokenVal)
	print("[FET_ITP]Sesssion Cookie :",sess.cookies.get_dict().get("PHPSESSID"))

	headers = {
		"User-Agent"	: "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:65.0) Gecko/20100101 Firefox/65.0",
		"Accept"	: "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
		"Accept-Encoding"	: "gzip, deflate",
		"Accept-Language"	:"en-US,en;q=0.5",
		"Referer"	:"http://fet.mmu.edu.my/itp/index_files/public_index.php?action=student_login",
		"Content-Type"	: "application/x-www-form-urlencoded",
		"Connection"	: "keep-alive",
		"Upgrade-Insecure-Requests"	:"1"
	}

	params = {
		"id":sid,
		"password":passw,
		"MyToken":pars.tokenVal,
		"Login":"Login"
	}

	url = "http://fet.mmu.edu.my/itp/index_files/public_index.php?action=student_login"
	reply = sess.post(url,headers=headers,data=params)
	print("Login reply code :",reply.status_code)
	return sess
