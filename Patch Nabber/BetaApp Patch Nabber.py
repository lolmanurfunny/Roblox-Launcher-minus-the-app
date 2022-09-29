from sys import exit
from time import sleep
from os import getenv, linesep, system
from os.path import exists
from urllib.request import urlopen, urlretrieve
from json import loads

DEBUG_MODE = False
REPO_PATH = "lolmanurfunny/Roblox-Launcher-minus-the-app"
ROBLOXPLAYER_NAME = "RobloxPlayerLauncher.exe"


def uac_error():
    input(
        "Did you install Roblox via running RobloxPlayerLauncher as administrator?\nTry reinstalling Roblox.\n"
        + "Don't open a new issue regarding this if you installed Roblox to a non-User directory!"
    )
    exit(1)


def get_filepath():
    response = urlopen(
        "https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag"
    ).read()

    zflag = loads(response)["clientVersionUpload"]
    print(f"Client version hash: {zflag}")
    filepath = f"{getenv('LOCALAPPDATA')}\Roblox\Versions\\"

    if not exists(filepath) or DEBUG_MODE:
        print('[Error]: Could not find the "\Roblox\Versions\\" folder!')
        uac_error()

    print('Found "\Roblox\Versions\\" folder!')
    filepath += zflag
    if exists(filepath):
        print(f'Found "{zflag}" folder!')
    else:
        print("[Error]: Unable to locate latest roblox client!")
        uac_error()

    return filepath


def reinsert_oof(filepath):
    location = f"{filepath}\content\sounds\ouch.ogg"
    oof = input("Would you like to return the oof sound back? [Y/N] ")

    if oof.strip().lower() == "y":
        print("Installing oof sound...")
        urlretrieve(f"https://github.com/{REPO_PATH}/raw/main/Audio/ouch.ogg", location)
        print("Successfully installed oof sound.")
    elif oof.strip().lower() == "n":
        print("Skipping...")
    else:
        print('You wrote neither "Y" nor "N". Skipping...')


def install_launcher(filepath):
    latest = (
        urlopen(
            f"https://raw.githubusercontent.com/{REPO_PATH}/main/Custom%20Launcher/latest"
        )
        .read()
        .decode()
        .rstrip(linesep)
    )
    # input(latest) # debuggerydoos
    print(f"Installing latest custom launcher from github! Version: {latest}")
    download = urlretrieve(
        f"https://github.com/{REPO_PATH}/releases/download/{latest}/{ROBLOXPLAYER_NAME}",
        f"{filepath}\\{ROBLOXPLAYER_NAME}",
    )
    print(f"File is located @{download.__getitem__(0)}")


if __name__ == "__main__":
    filepath = get_filepath()
    install_launcher(filepath)
    reinsert_oof(filepath)
    print("This window will close in 3 seconds...")

    for i in range(3, 0, -1):
        system("title " + f"Closing in {i}")
        print(".")
        sleep(1)
