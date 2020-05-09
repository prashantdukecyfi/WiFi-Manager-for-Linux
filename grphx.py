from tkinter import *
import os, sys, subprocess
from wifid import WiFiD
"""
Created By- Prashant Raj, 16/IT/33
"""

class Grphx:
	pos = 0
	netwrkx = list()
	netname = list()
	def __init__(self):
		self._root = Tk()
		self.wifiObj = WiFiD()
		self._root.title("WiFi-D")
		self._root.minsize(358,450)
		self.scrollbar = Scrollbar(self._root)
		#self.scrollbar.grid(row = 0, rowspan=15, column=7)
		self.image1 = PhotoImage(file = "pngk.png")
		imglabel = Label(self._root, image = self.image1).grid(row = 0, column = 0, rowspan = 2, columnspan = 3, sticky ="E", ipady = 5, pady=(10,30))
		label1 = Label(self._root, text = "WiFi-D")
		label1.configure(font = ("Verdana", 24, "bold", "italic"))
		label1.grid(row = 0, column = 3, rowspan = 2, columnspan = 3, sticky ="W", pady=(10,30))
		self.scan(1)
		global pos
		pos = pos + 5
		strng = "* denotes the presently connected network!"
		label2 = Label(self._root, text = strng).grid(row = pos, column = 0, rowspan = 1, columnspan = 6, pady = (30,40))
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
		btn = Button(self._root, text = "Connect", command = lambda : self.scan(3))
		btn.configure(font = ("Verdana", 10, "bold"))
		btn.grid(row = pos+7, column=0, columnspan=6, sticky = "EW", ipady=3)
		#self.scrollbar.config(command = self._root.yview)
		self._root.mainloop()
		
	def scan(self, num):
		global netwrkx
		if num == 1:
			netwrkx = self.wifiObj.scanWiFi()
			self.showWiFi(netwrkx)
		elif num == 2:
			self.wifiObj.restartWiFi()
			netwrkx = self.wifiObj.scanWiFi()
			self.showWiFi(netwrkx)
		elif num == 3:
			self.connectToWiFi(netwrkx)
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
		self.netname.append(var)
		Label(self._root, text = str(i+1)).grid(row=i+6, column=0, columnspan=2, sticky = "EW")
		Label(self._root, text = var).grid(row=i+6, column=2, columnspan=2, sticky = "EW")
		Label(self._root, text = strength).grid(row=i+6, column=4, columnspan=2, sticky = "EW")
	
	def connectToWiFi(self, nets):
		self.page2 = Tk()
		self.page2.title("WiFi-D: Connect to WiFi")
		#self.page2.minsize(250,450)
		list1 = Listbox(self.page2)
		list1.pack()
		for i in range(len(self.netname)):
			list1.insert(END, self.netname[i])
		self.page2.mainloop()
		
		
