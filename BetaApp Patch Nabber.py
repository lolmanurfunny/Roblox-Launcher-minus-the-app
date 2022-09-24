from sys import exit
from time import sleep
from os import getenv
from os.path import exists
from urllib.request import urlopen, urlretrieve
from json import loads

a = urlopen("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag").read()
a = loads(a)["clientVersionUpload"]
print("Client version hash: "+a)
filepath = os.getenv("LOCALAPPDATA")+"\Roblox\Versions\\"

if exists(filepath):
    print("Found \"\Roblox\Versions\\\" folder!")
    filepath+=a
    if exists(filepath):
        print("Found \""+a+"\" folder!")
    else:
        input("[Error]: Unable to locate latest roblox client!")
        exit()
else:
    input("[Error]: Could not find the \"\Roblox\Versions\\\" folder!")
    exit()
rpl = "RobloxPlayerLauncher.exe"

print("Downloading latest patched launcher from github!")
download = urlretrieve("https://github.com/lolmanurfunny/Roblox-Launcher-minus-the-app/raw/main/"+rpl,filepath+"\\"+rpl)


print("File is located @",download.__getitem__(0)+"\nThis window will close in 3 seconds...")
for _ in range(0,3):
    sleep(.5)
    print('.')
    sleep(.5)
exit(1)
