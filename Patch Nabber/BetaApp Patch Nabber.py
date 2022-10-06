from sys import exit
from time import sleep
from os import getenv, linesep, system, remove
from os.path import exists, dirname, realpath
from urllib.request import urlopen, urlretrieve
from json import loads
from subprocess import Popen

absPath = dirname(realpath(__file__))

a = urlopen("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag").read()
a = loads(a)["clientVersionUpload"]
print("Client version hash: "+a)
filepath = getenv("LOCALAPPDATA")+"\Roblox\Versions\\"
isOld = False

def littleTimmyPrevention():
    input("Did you install Roblox via running RobloxPlayerLauncher as administrator?\nTry reinstalling Roblox.\nDon't open a new issue regarding this if you installed Roblox to a non-User directory!")

debug = False
if exists(filepath) and not debug:
    print("Found \"\Roblox\Versions\\\" folder!")
    filepath+=a
    if exists(filepath):
        print("Found \""+a+"\" folder!")
    else:
        isOld = True
        print("[Error]: Unable to locate latest roblox client! Installing it automatically.")
        #lmao roblox updater??!??!
        #install robloxplayerlauncher then delete it, this is just for updating
        setupPage = "https://setup.rbxcdn.com/{}-Roblox.exe".format(a)
        latest = urlretrieve(setupPage, "RobloxPlayerLauncher.exe")
        proc = Popen("{}\\RobloxPlayerLauncher.exe".format(absPath))
        proc.wait()
else:
    print("[Error]: Could not find the \"\Roblox\Versions\\\" folder!")
    littleTimmyPrevention()
    exit(1)

rpl = "RobloxPlayerLauncher.exe"

location1 = filepath+"\\"+rpl
location2 = filepath+"\content\sounds\ouch.ogg"

repo = "lolmanurfunny/Roblox-Launcher-minus-the-app"
latest = urlopen("https://raw.githubusercontent.com/"+repo+"/main/Custom%20Launcher/latest").read().decode().rstrip(linesep)
#input(latest) # debuggerydoos
print("Installing latest custom launcher from github! Version: "+latest)
download = urlretrieve("https://github.com/"+repo+"/releases/download/"+latest+"/"+rpl,location1)

print("File is located @",download.__getitem__(0))

if isOld == True:
    remove("{}\\RobloxPlayerLauncher.exe".format(absPath))


oof = input("Would you like to return the oof sound back? [Y/N] ")

if oof.lower().strip() == "y":
    print("Installing oof sound...")
    urlretrieve("https://github.com/"+repo+"/raw/main/Audio/ouch.ogg",location2)
    print("Successfully installed oof sound.")
elif oof.lower().strip() == "n":
    print("Skipping...")
else:
    print("You wrote neither \"Y\" nor \"N\". Skipping...")

print("This window will close in 3 seconds...")

for _ in range(3,0,-1):
    system("title "+"Closing in "+_.__str__())
    print('.')
    sleep(1)
exit(0) # now exiting with a non-non-zero value :D
