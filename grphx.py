from tkinter import *
import os, sys, subprocess
from wifid import WiFiD
class Grphx:
	pos = 0
	def __init__(self):
		self._root = Tk()
		self.wifiObj = WiFiD()
		self._root.title("WiFi-D")
		self._root.minsize(358,450)
		self.image1 = PhotoImage(file = "pngk.png")
		imglabel = Label(self._root, image = self.image1).grid(row = 0, column = 0, rowspan = 2, columnspan = 3, ipady = 5, pady=(10,30))
		label1 = Label(self._root, text = "WiFi-D")
		label1.configure(font = ("Verdana", 24, "bold", "italic"))
		label1.grid(row = 0, column = 3, rowspan = 2, columnspan = 3, sticky ="W", pady=(10,30))
		self.scan(1)
		
		
		
		
		
		global pos
		pos = pos + 5
		
		
		
		label2 = Label(self._root, text = "* denotes the presently connected network!").grid(row = pos, column = 0, rowspan = 1, columnspan = 6, pady = (30,40))
		pos = pos + 5
		btn1 = Button(self._root, text = "Scan WiFi Networks", command = lambda : self.scan(1))
		btn1.configure(font = ("Verdana", 10, "bold"))
		btn1.grid(row = pos+3, column=0, columnspan=3, sticky = "EW", ipady = 3)
		btn2 = Button(self._root, text = "Exit WiFi-D", command = lambda : self.scan(0))
		btn2.configure(font = ("Verdana", 10, "bold"))
		btn2.grid(row = pos+3, column=3, columnspan=3, sticky = "EW", ipady = 3)
		btn3 = Button(self._root, text = "Restart WiFi Manager", command = lambda : self.scan(2))
		btn3.configure(font = ("Verdana", 10, "bold"))
		btn3.grid(row = pos+5, column=0, columnspan=6, sticky = "EW", ipady = 3)
		
		
		
		
		self._root.mainloop()
		
	def scan(self, num):
		if num == 1:
			netwrkx = self.wifiObj.scanWiFi()
			self.showWiFi(netwrkx)
		elif num == 2:
			self.wifiObj.restartWiFi()
			netwrkx = self.wifiObj.scanWiFi()
			self.showWiFi(netwrkx)
		elif num == 0:
			exit(0)
	def showWiFi(self, nets):
		#self.page2 = Tk()
		#self.page2.title("WiFi-D: Available Networks")
		#self.page2.minsize(250,450)
		#self.page2.configure(background = "grey")
		length = len(nets)
		label1 = Label(self._root, text = "Serial Number")
		label1.configure(font = ("Verdana", 14, "bold"))
		label1.grid(row=5, column=0, columnspan=2, sticky = "EW", ipady=5, ipadx = 10)
		label2 = Label(self._root, text = "Network ID")
		label2.configure(font = ("Verdana", 14, "bold"))
		label2.grid(row=5, column=2, columnspan=2, sticky = "EW", ipady=5, ipadx = 10)
		label3 = Label(self._root, text = "Network Strength")
		label3.configure(font = ("Verdana", 14, "bold"))
		label3.grid(row=5, column=4, columnspan=2, sticky = "EW", ipady=5, ipadx = 10)
		i = 0
		for i in range(length):
			self.draw(nets[i],i)
		global pos
		pos = i + 6
	def draw(self, nets, i):
		var = ""
		c = 0
		strength = 0
		for j in nets:
			if j != 'Infra' and c == 0:
				var = var + j
			elif j == 'Mbit/s' and c == 1:
				strength = nets[nets.index(j)+1]
				break
			else:
				c = 1
		Label(self._root, text = str(i+1)).grid(row=i+6, column=0, columnspan=2, sticky = "EW")
		Label(self._root, text = var).grid(row=i+6, column=2, columnspan=2, sticky = "EW")
		Label(self._root, text = strength).grid(row=i+6, column=4, columnspan=2, sticky = "EW")
		
		
		
		
