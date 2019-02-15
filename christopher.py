#!/usr/bin/python3
# Christopher.py is a python program designed to dig out uploaded academic results
# of MMU FOE ITP student.
# created by Yeo Kai Shun and Chia Jason

#ar - academic results

#allows HTTP requests
import requests
from html.parser import HTMLParser

#this module disable printing of keystrokes
import getpass

#custom libs
from auth import fet

class MyHTMLParser(HTMLParser):
	errorFlag = False
	def handle_starttag(self,tag,attrs):
		pass
	def handle_endtag(self,tag):
		pass
	def handle_data(self,data):
		if(data=='alert("There is some error. Please try again.")'):
			self.errorFlag = True

#actual script usage code
if __name__ == "__main__":
	#target domain setup
	#conn setup
	host_domain_name = "fet.mmu.edu.my"
	https_url_format = "https://{}:{}/itp/index_files/student_index.php?action=rf&o=r&n={}"
	https_req_portnm = 443

	#http settings (not used)
	http_url_format = "http://{}:{}/itp/index_files/student_index.php?action=rf&o=r&n={}"
	http_req_portnm = 80

	test_id = "1161300548"
	passw = getpass.getpass("Please enter password for "+test_id+" :")
	auth_sess = fet.login(test_id,passw)

	#URL manip prefix 
	# possible format - YMDHMS
	dt_true  = "181001072031" #to observe what happens when a true ar returns
	dt_false = "181002072031" #to observe what happens when a false return 
	dt_target = dt_true #testline
	
	req_url = http_url_format.format(host_domain_name,http_req_portnm,dt_target+test_id)
	print("Requesting with datetime :",dt_true)
	print("Request URL :",req_url)
	
	r = auth_sess.get( req_url )
	checkparse = MyHTMLParser()
	checkparse.feed(r.text)
	if(checkparse.errorFlag):
		print("datetime is false.")
	else:
		print("datetime is true.")
   
