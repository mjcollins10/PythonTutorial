# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 16:50:02 2015

@author: mcollins
"""

import os, re, threading

class ip_check(threading.Thread):
   """ping given address""" 
   def __init__ (self,ip):
      threading.Thread.__init__(self)
      self.ip = ip
      self.__successful_pings = -1
      
   def run(self):
      ping_out = os.popen("ping -q -c2 "+self.ip,"r")
      while True:
        line = ping_out.readline()
        if not line: break
        n_received = re.findall(received_packages,line)
        if n_received:
           self.__successful_pings = int(n_received[0])
           
   def status(self):
      if self.__successful_pings == 0:
         return "no response"
      elif self.__successful_pings == 1:
         return "alive, but 50 % packet loss"
      elif self.__successful_pings == 2:
         return "alive"
      else:
         return "shouldn't occur"
         
received_packages = re.compile(r"(\d) packets received")

check_results = []
for suffix in range(120,131):
   ip = "137.156.2."+str(suffix)
   current = ip_check(ip)
   check_results.append(current)
   current.start()

for el in check_results:
   el.join()
   print("Status from ", el.ip,"is",el.status())