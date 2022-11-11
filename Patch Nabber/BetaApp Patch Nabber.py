from sys import exit
from time import sleep
from os import getenv, system, rename
from os.path import exists
from urllib.request import urlopen, urlretrieve
from json import loads

a = urlopen("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag").read()
a = loads(a)["clientVersionUpload"]
print("Client version hash: "+a)
filepath = getenv("LOCALAPPDATA")+"\Roblox\Versions\\"

def littleTimmyPrevention():
    input("Did you install Roblox via running RobloxPlayerLauncher as administrator?\nTry reinstalling Roblox.\nDon't open a new issue regarding this if you installed Roblox to a non-User directory!")

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

# rpl = "RobloxPlayerLauncher.exe"

# location1 = filepath+"\\"+rpl
ExtraContent = filepath+"\ExtraContent"

places = ExtraContent+"\\places"
# 🤓 (anyone else notice how there's no skin tone for the nerd emoji, bros perma asian)
UniversalApp = ExtraContent+"\\LuaPackages\\UniversalApp"

ouch = filepath+"\content\sounds\ouch.ogg"

# places folder is the only one that matters here, but why not also prevent roblox from loading uNiVeRSaLaPp too while we're at it.
if exists(places) and not debug:
    rename(places,ExtraContent+"\\places_But_better") # not adding an "else" block if this doesn't work on your first execution per update (don't fucking make an issue)
    if exists(UniversalApp):
        rename(UniversalApp,ExtraContent+"\\LuaPackages\\"+"shitty idea on roblox's part ngl")
# lord forgive me for doing this even though at the end of the day I'm still parting the sea.

repo = "lolmanurfunny/Roblox-Launcher-minus-the-app"
# latest = urlopen("https://raw.githubusercontent.com/"+repo+"/main/Custom%20Launcher/latest").read().decode().rstrip(linesep)
#input(latest) # debuggerydoos
# print("Installing latest custom launcher from github! Version: "+latest)
# download = urlretrieve("https://github.com/"+repo+"/releases/download/"+latest+"/"+rpl,location1)

# print("File is located @",download.__getitem__(0))




oof = input("Would you like to return the oof sound back? [Y/N] ")

if oof.lower() == "y".strip():
    print("Installing oof sound...")
    urlretrieve("https://github.com/"+repo+"/raw/main/Audio/ouch.ogg",ouch)
    print("Successfully installed oof sound.")
elif oof.lower() == "n".strip():
    print("Skipping...")
else:
    print("You wrote neither \"Y\" nor \"N\". Skipping...")

print("This window will close in 3 seconds...")

for _ in range(3,0,-1):
    system("title "+"Closing in "+_.__str__())
    print('.')
    sleep(1)
exit(0) # now exiting with a non-non-zero value :D