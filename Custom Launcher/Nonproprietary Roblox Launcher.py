#===============================================#
#|  Nonproprietary Roblox Launcher   [v1.0.0]  |#
#===============================================#
from argparse import ArgumentParser
from urllib.request import urlopen
from urllib.parse import unquote
from subprocess import Popen
from time import sleep
from json import loads
from sys import exit
import os
import re


parser = ArgumentParser()
parser.add_argument("a")
args = parser.parse_args().a
found = re.split("\+",args)

s = [re.split(":",_)[1] for _ in found]
args = "--InBrowser -t "+s[2]+" -j "+"\""+unquote(s[4])+"\""+" -b "+s[5]+" --launchtime="+s[3]+" --rloc "+s[6]+" --gloc "+s[7]+" -channel zflag"
s,_ = re.subn(s[2],r"***********",args) # Censoring auth ticket, I don't like that entirely being visible on screen, word-wrap doesn't help either lol
print(s)

clientHash = loads(urlopen("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag").read())["clientVersionUpload"]
print("Client version hash: "+clientHash)
filepath = os.getenv("LOCALAPPDATA")+"\Roblox\Versions\\"

if os.path.exists(filepath):
    print("Found \"\Roblox\Versions\\\" folder!")
    filepath+=clientHash
    if os.path.exists(filepath):
        print("Found \""+clientHash+"\" folder!")
    else:
        input("[Error]: Unable to locate latest roblox client!")
        exit()
else:
    input("[Error]: Could not find the \"\Roblox\Versions\\\" folder!")
    exit()

line = filepath+"\\RobloxPlayerBeta.exe "+args
#os.system(line) <-- caused some headaches, couldn't close the window automatically
print("Launching!")
launcher = Popen(line)
print("This window will close in 5 seconds.")
sleep(5)
exit(0)
# :)
