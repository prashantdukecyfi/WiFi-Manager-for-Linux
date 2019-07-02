from wifid import WiFiD
from grphx import Grphx
class RunWiFiD(Grphx):
	def __init__(self):
		self.wifi = WiFiD()
		super(RunWiFiD, self).__init__()
	
obj = RunWiFiD()
