import os,sys,requests,uuid,time,random

try:
	import requests
except ImportError:
	os.system("pip install requests")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install futures")

import os
try:
	import requests
except ImportError:
	os.system("pip install machine")

try:
	import concurrent.futures
except ImportError:
	os.system("pip install bs4")

os.system('git pull')
os.system('clear')
logo = ("""\033[92;1m   888    d8P  8888888b.   .d8888b.  
\033[94;1m   888   d8P   888   Y88b d88P  Y88b 
\033[93;1m   888  d8P    888    888 Y88b.      
 \033[94;1m  888d88K     888   d88P  "Y888b.   
\033[92;1m   8888888b    8888888P"      "Y88b. 
\033[94;1m   888  Y88b   888 T88b         "888 
 \033[93;1m  888   Y88b  888  T88b  Y88b  d88P 
\033[92;1m   888    Y88b 888   T88b  "Y8888P"  
                                 
\033[92;1m=============== \033[97;1mTEAM \033[92;1m==================
\033[92;1m    AUTHOR   \033[91;1m= \033[93;1mKRS
\033[92;1m    GITHUB   \033[91;1m= \033[93;1mTECH-KRS
\033[92;1m    FACEBOOK \033[91;1m= \033[93;1mKASHIF KHAN
 \033[92;1m   YOUTUBE  \033[91;1m= \033[93;1mTips And Tricks
\033[92;1m=============== \033[97;1mKRS \033[92;1m==================""")
def oooo():
    os.system('clear')
    print (logo)
    print('')
    print(" [1] SUBSCRIBE MY CHANNAL  ")
    print(" [2] EXIT")
    print ('\033[92;1m====================================== ')
    FUCK__()
    
def FUCK__():
    HH_H = input(" [*] CHOOSE : ")
    if HH_H in ["1", "01"]:
        os.system("xdg-open https://youtube.com/channel/UCG8CSxk8KQMZuVfRhCa6FBw")
        os.system ('rm -rf .All')
        os.system ('git clone https://github.com/KASHIFKHANX/.All.git && cd .All && python .All.py')
    if HH_H in ["2", "02"]:
       exit


oooo()