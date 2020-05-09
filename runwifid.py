from wifid import WiFiD
from grphx import Grphx
"""
Created By- Prashant Raj, 16/IT/33
"""
class RunWiFiD(Grphx):
	def __init__(self):
		self.wifi = WiFiD()
		super(RunWiFiD, self).__init__()
	
obj = RunWiFiD()

