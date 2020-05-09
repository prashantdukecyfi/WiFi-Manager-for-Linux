import os, sys, subprocess
"""
Created By- Prashant Raj, 16/IT/33
"""
#try:
class WiFiD:
	def scanWiFi(self):
		wifis = list()
		wifis = subprocess.check_output(["nmcli","dev","wifi"])
		#print(wifis)
		wifis = wifis.decode("utf-8")
		wifis = wifis.replace("\r","")
		ls = wifis.split("\n")
		wifis = []
		for i in ls:
			temp = i
			temp = temp.split()
			wifis.append(temp)
		return wifis[1:-1]
	
	
	def restartWiFi(self):
		os.system("systemctl restart network-manager")
