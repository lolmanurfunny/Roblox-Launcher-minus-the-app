from sys import exit
from time import sleep
from os import getenv, linesep, system, remove
from shutil import rmtree
from os.path import exists, dirname, realpath
from urllib.request import urlopen, urlretrieve
from json import load
from subprocess import Popen

absPath = dirname(realpath(__file__))

def littleTimmyPrevention():
    input("Did you install Roblox via running RobloxPlayerLauncher as administrator?\nTry reinstalling Roblox.\nDon't open a new issue regarding this if you installed Roblox to a non-User directory!")
    
isOld = False


ver = load(urlopen("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag"))["clientVersionUpload"]
print("Client version hash: "+ver)

filepath = getenv("LOCALAPPDATA")+"\Roblox\Versions\\"

debug = False
if exists(filepath) and not debug:
    print("Found \"\Roblox\Versions\\\" folder!")
    filepath+=ver
    if exists(filepath):
        print("Found \""+ver+"\" folder!")
    else:
        isOld = True
        print("[Error]: Unable to locate latest roblox client! Installing it automatically.")
        #lmao roblox updater??!??!
        #install robloxplayerlauncher then delete it, this is just for updating
        setupPage = "https://setup.rbxcdn.com/{}-Roblox.exe".format(ver)
        latest = urlretrieve(setupPage, "RobloxPlayerLauncher.exe")
        proc = Popen("{}\\RobloxPlayerLauncher.exe".format(absPath))
        proc.wait()   
elif not exists(getenv("LOCALAPPDATA")+"\\Roblox\\"):
    #the thing doesnt exist that means it WILL error when installing, back out
    print("[FATAL ERROR]: Cannot install modified Roblox Client to Program Files(x86)")
    littleTimmyPrevention()
    exit(1)

rpl = "RobloxPlayerLauncher.exe"

location1 = filepath+"\\"+rpl
location2 = filepath+"\content\sounds\ouch.ogg"

repo = "lolmanurfunny/Roblox-Launcher-minus-the-app"
latest = urlopen("https://raw.githubusercontent.com/"+repo+"/main/Custom%20Launcher/latest").read().decode().rstrip(linesep)
latestScript = urlopen("https://raw.githubusercontent.com/lolmanurfunny/Roblox-Launcher-minus-the-app/main/Custom%20Launcher/Nonproprietary%20Roblox%20Launcher.py")
with open("RobloxPlayerLauncher.py", "wb") as f:
    f.write(latestScript.read())

system('cmd /c "pyinstaller --onefile RobloxPlayerLauncher.py"')
system('cmd /c "xcopy {}\\dist\\RobloxPlayerLauncher.exe  {} /y /s"'.format(absPath, filepath))
remove("{}\\RobloxPlayerLauncher.py".format(absPath))
rmtree("{}\\build".format(absPath))
remove("{}\\RobloxPlayerLauncher.spec".format(absPath))
rmtree("{}\\dist".format(absPath))
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