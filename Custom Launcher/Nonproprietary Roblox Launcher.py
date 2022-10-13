#===============================================#
#|  Nonproprietary Roblox Launcher   [v1.1.1]  |#
#===============================================#

from argparse import ArgumentParser
from urllib.parse import unquote
from subprocess import Popen
#from time import sleep,time
from os.path import dirname, realpath, exists
from re import split#,subn
from os import system, getenv
from sys import exit,executable
from ctypes import windll
from urllib.request import urlopen, urlretrieve
from json import loads
windll.kernel32.SetConsoleTitleW("Nonproprietary Roblox Launcher v1.1.0 | By: lolmanurfunny <3")
#ts = time() # benchmarking
def littleTimmyPrevention():
    input("Roblox has encountered a fatal error. Don't install Roblox as Administrator.")
    
a = urlopen("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag").read()
a = loads(a)["clientVersionUpload"]

filepath = getenv("LOCALAPPDATA")+"\Roblox\Versions\\"

absPath = dirname(realpath(__file__))


#lemme just do some checks :tehee:
if exists(filepath):
    filepath+=a
    if not exists(filepath):
        print("[Error]: Unable to locate latest roblox client! Installing it automatically.")
        setupPage = "https://setup.rbxcdn.com/{}-Roblox.exe".format(a)
        latest = urlretrieve(setupPage, "RobloxPlayerLauncher.exe")
        proc = Popen("{}\\RobloxPlayerLauncher.exe".format(absPath))
        proc.wait()   
elif not exists(getenv("LOCALAPPDATA")+"\\Roblox\\"):
    #the thing doesnt exist that means it WILL error when installing, back out
    print("[FATAL ERROR]: Cannot install modified Roblox Client to Program Files(x86)")
    littleTimmyPrevention()
    exit(1)

def jimbo():
    system("cls");system("start https://github.com/lolmanurfunny/Roblox-Launcher-minus-the-app");exit(0)

dir = dirname(executable) #path of exe
parser = ArgumentParser()
parser.add_argument("a")
args = ""
try:
    args = parser.parse_args().__str__()
except:
    jimbo()

found = split("\+",args)
s = [split(":",_)[1] for _ in found]
args = "--InBrowser -t "+s[2]+" -j "+"\""+unquote(s[4])+"\""+" -b "+s[5]+" --launchtime="+s[3]+" --rloc "+s[6]+" --gloc "+s[7]+" -channel zflag"
#s,_ = subn(s[2],r"***********",args) # Censoring auth ticket, I don't like that entirely being visible on screen, word-wrap doesn't help either lol
#print(s)
if dir.find("\\Roblox\\Versions\\version") == -1:
    exit(1)
Popen(dir+"\\RobloxPlayerBeta.exe "+args)
#filepath = filepath or getenv("LOCALAPPDATA")+"\Roblox\Versions\\"
#clientHash = clientHash or loads(urlopen("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag").read())["clientVersionUpload"]
#print("Client version hash: "+dir.split("\\").pop())
#print("Launching!")
# Don't tell me you thought we were launching when we said we were? 🙃
#print("Took "+(time()-ts).__str__()+" seconds!")
#print("This window will close in 5 seconds.")
#sleep(5-.25)# optimized👽
exit(0)
# :)
