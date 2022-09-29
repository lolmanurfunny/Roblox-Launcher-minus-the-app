# ===============================================#
# |  Nonproprietary Roblox Launcher   [v1.1.1]  |#
# ===============================================#

from argparse import ArgumentParser
from urllib.parse import unquote
from subprocess import Popen

# from time import sleep,time
from os.path import dirname
from re import split  # ,subn
from os import system
from sys import exit, executable
from ctypes import windll

windll.kernel32.SetConsoleTitleW(
    "Nonproprietary Roblox Launcher v1.1.0 | By: lolmanurfunny <3"
)
# ts = time() # benchmarking


def redo_process():
    system("cls")
    system("start https://github.com/lolmanurfunny/Roblox-Launcher-minus-the-app")
    exit(0)


def gen_args():
    parser = ArgumentParser()
    parser.add_argument("a")
    arg_str = ""
    try:
        arg_str = parser.parse_args().__str__()
    except:
        redo_process()

    splits = [split(":", _)[1] for _ in split("\+", arg_str)]
    return (
        "--InBrowser -t "
        + splits[2]
        + " -j "
        + '"'
        + unquote(splits[4])
        + '"'
        + " -b "
        + splits[5]
        + " --launchtime="
        + splits[3]
        + " --rloc "
        + splits[6]
        + " --gloc "
        + splits[7]
        + " -channel zflag"
    )


if __name__ == "__main__":
    dir = dirname(executable)  # path of exe
    # Censoring auth ticket, I don't like that entirely being visible on screen, word-wrap doesn't help either lol
    # s,_ = subn(s[2],r"***********",args)
    # print(s)
    args = gen_args()
    if dir.find("\\Roblox\\Versions\\version") == -1:
        exit(1)
    Popen(f"{dir}\\RobloxPlayerBeta.exe " + args)
    # filepath = filepath or getenv("LOCALAPPDATA")+"\Roblox\Versions\\"
    # clientHash = clientHash or loads(urlopen("https://clientsettingscdn.roblox.com/v2/client-version/WindowsPlayer/channel/zflag").read())["clientVersionUpload"]
    # print("Client version hash: "+dir.split("\\").pop())
    # print("Launching!")
    # Don't tell me you thought we were launching when we said we were? 🙃
    # print("Took "+(time()-ts).__str__()+" seconds!")
    # print("This window will close in 5 seconds.")
    # sleep(5-.25)# optimized👽
    exit(0)
    # :)
