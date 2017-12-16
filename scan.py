#!usr/bin/python
# -*- coding: utf-8 -*-
#import zone
#Coded By Badreddine CHamkhi DOn't Change Rights :) 
#alfallaga team <3
#fallag error105	
#done while listening to psyco'm plume 
#Sat 15:37 ====> Sat 17:08
#./DOne
import urllib2
import os
from platform import system 
import re 
import sys 
###################Clear Screen###############################################
def clear():
	if system() == 'Linux':
		os.system('clear')
	if system() == 'Windows':
		os.system('cls')
clear()
###########################Banner########################### 
banner = '''\033[1;34m 
	[ Wordpress Job Manager Scanner For Post-A-Job Exploit ]
	[ Dork : inurl:wp-content/uploads/job-manager-uploads/ ]
	\033[1;31m[ Coded By Fallag Error105 | Badreddine CHamkhi ]\033[1;m
\033[1;m
'''
print banner 
######################RealShit :) ########################### 


def unique(zeb):
    badr = set()
    return [badr.add(x) or x for x in zeb if x not in badr]


def scan(site):
	try:
		print "\033[1;33m[+] Scanning :\033[1;m "+str(site)
		terma = urllib2.urlopen(str(site)+"/post-a-job/").read()
		if('<form action="/post-a-job/" method="post" id="submit-job-form" class="job-manager-form" enctype="multipart/form-data">' in terma):
			print "  \033[1;32mVuln => :\033[1;m "+str(site)+"/post-a-job/"
			with open("Vuln.txt", "a") as f:
				f.write(site+"\n")
		else:
			print " Not Vuln "
	except:
		pass
#Main
try:
	file = open(sys.argv[1]).readlines()
except :
	print "Usage : "+str(sys.argv[0])+" list.txt"
	print " Please Pick A List From The Script File "
	sys.exit(1)
if(len(file) > 0):	
	for s in file:
		s = s.rstrip()
		scan(s)


		
print "\n\033[1;46mResults Will Be Shown In vuln.txt In The Script File\033[1;m"
