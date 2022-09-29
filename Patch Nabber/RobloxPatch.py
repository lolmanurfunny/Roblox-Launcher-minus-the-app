from sys import exit
from time import sleep
import os
from os.path import exists
from urllib.request import urlopen, urlretrieve
from json import loads

absPath = os.path.dirname(os.path.realpath(__file__))

def littleTimmyPrevention():
    littleTimmyPrevention()
    exit(1)


a = urlopen("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag").read()
a = loads(a)["clientVersionUpload"]
print("Client version hash: "+a)

filepath = os.getenv("LOCALAPPDATA")+"\Roblox\Versions\\"

debug = False
if exists(filepath) and not debug:
    print("Found \"\Roblox\Versions\\\" folder!")
    filepath+=a
    if exists(filepath):
        print("Found \""+a+"\" folder!")
    else:
        print("[Error]: Unable to locate latest roblox client!")
        littleTimmyPrevention()
        exit(1)
else:
    print("[Error]: Could not find the \"\Roblox\Versions\\\" folder!")
    littleTimmyPrevention()
    exit(1)

rpl = "RobloxPlayerLauncher.exe"

location1 = filepath+"\\"+rpl
location2 = filepath+"\content\sounds\ouch.ogg"

repo = "lolmanurfunny/Roblox-Launcher-minus-the-app"
latest = urlopen("https://raw.githubusercontent.com/"+repo+"/main/Custom%20Launcher/latest").read().decode().rstrip(os.linesep)
latestScript = urlopen("https://raw.githubusercontent.com/lolmanurfunny/Roblox-Launcher-minus-the-app/main/Custom%20Launcher/Nonproprietary%20Roblox%20Launcher.py")
with open("RobloxPlayerLauncher.py", "wb") as f:
    f.write(latestScript.read())

os.system('cmd /c "pyinstaller --onefile RobloxPlayerLauncher.py"')
os.system('cmd /c "xcopy {}\\dist\\RobloxPlayerLauncher.exe  {} /y /s"'.format(absPath, filepath))
os.system('cmd /c "del /f {}\\RobloxPlayerLauncher.py"'.format(absPath))
os.system('cmd /c "rmdir /s /q {}\\build"'.format(absPath))
os.system('cmd /c "del /f {}\\RobloxPlayerLauncher.spec"'.format(absPath))
os.system('cmd /c "rmdir /s /q {}\\dist"'.format(absPath))

oof = input("Would you like to return the oof sound back? [Y/N] ")

if oof.lower() == "y".strip():
    print("Installing oof sound...")
    urlretrieve("https://github.com/"+repo+"/raw/main/Audio/ouch.ogg",location2)
    print("Successfully installed oof sound.")
elif oof.lower() == "n".strip():
    print("Skipping...")
else:
    print("You wrote neither \"Y\" nor \"N\". Skipping...")


print("This window will close in 3 seconds...")

for _ in range(3,0,-1):
    os.system("title "+"Closing in "+_.__str__())
    print('.')
    sleep(1)
exit(0) # now exiting with a non-non-zero value :D