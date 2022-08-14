import re
import subprocess
import sys
import signal
import os
from threading import Timer
from uuid import uuid4
from functools import partial
from pynput.keyboard import Key
from platform import platform

ispaused = False

_dir = os.getcwd()

class PauseException(Exception):
    pass

COLORS_WITH_CODES = {
    "black": "\x1B[30m",
    "bg-black": "\x1B[40m",
    "red": "\x1B[31m",
    "bg-red": "\x1B[41m",
    "green": "\x1B[32m",
    "bg-green": "\x1B[42m",
    "yellow": "\x1B[33m",
    "bg-yellow": "\x1B[43m",
    "blue": "\x1B[34m",
    "bg-blue": "\x1B[44m",
    "white": "\x1B[37m",
    "bg-white": "\x1B[47m",
    "clear": "\x1B[0m ",
    "none": ""
}



def customexit():
    if "windows" in platform().lower():
        os._exit(0)
    else:
        os.kill(os.getpid(), signal.SIGINT)

def clear():
    
def pause_or_play():
    global ispaused
    ispaused = not ispaused
    if ispaused:
        print("===> PAUSED")
    else:
        print("===> RESUMING...")

def change_branch(newbranch):
    global ispaused
    global _dir
    print("Changing branch")
    force_pause = not ispaused
    if force_pause:
        pause_or_play()
    setbranch(_dir, newbranch)

KEYS_WITH_ACTIONS = {
    "'q'": customexit,
    "'p'": pause_or_play
}

def param_dict(arr):
    classified = {}
    for el in arr:
        try:
            destructered = el.rsplit('=')
            if len(destructered) == 1:
                classified[destructered[0]] = True
            else:
                classified[destructered[0]] = destructered[1]

        except Exception as e:
            print(e)
    return classified

def colorcode(text, color = '', bg = ''):
    color = COLORS_WITH_CODES.get(color, "")
    bg = COLORS_WITH_CODES.get(bg, "")
    # if color == 'none' and bg == 'none':
    #     return f'{text}'

    # if bg == 'none':
    #     return f'{COLORS_WITH_CODES[color]}{text}{COLORS_WITH_CODES["clear"]}'
    
    return f'{color}{bg}{text}{COLORS_WITH_CODES["clear"]}'

def setbranch(dir, branch):
    global _dir
    _dir = dir
    try:
        subprocess.call(["git", "-C", dir, "branch", "-M", branch])
        print("--> Set Branch to {br}".format(br=colorcode(branch, "green")))
    except Exception as e:
        print("{error}".format(error=colorcode(repr(e), "white", "bg-red")))
        customexit()

def commit_message(template):
    if re.search("#num#", template):
        template = re.sub("#num#", uuid4().hex, template)
    else:
        template = f'{template}-{uuid4().hex}'
    return template


def push(ct, dir, branch, interval, beforemethod=None):
    global ispaused
    try:
        global ispaused
        if ispaused:
            raise PauseException
        if beforemethod:
            beforemethod()
        print("\n--> Pushing to {br}".format(br=colorcode(branch, "green")))
        subprocess.call(["git", "-C", dir, "add", "."], stdout=subprocess.DEVNULL)
        # print("--> Set Branch to {br}".format(br=colorcode(branch, "green")))
        subprocess.call(["git", "-C", dir, "commit", "-m", "{m}".format(m=commit_message(ct))], stdout=subprocess.DEVNULL)
        # print("--> Set Branch to {br}".format(br=colorcode(branch, "green")))
        subprocess.call(["git", "-C", dir, "push", "origin", branch], stdout=subprocess.DEVNULL)
        print("--> Pushed to {br}".format(br=colorcode(branch, "green")))
    except PauseException:
        pass
    except Exception as e:
        print("{error}".format(error=colorcode(repr(e), "white", "bg-red")))
        customexit()
    finally:
        Timer(interval*60, partial(push, ct, dir, branch, interval, beforemethod)).start()

def test_push(ct, dir, branch, interval):
    print(f"got these {ct}, {dir}, {branch}, {interval}")
    Timer(interval*60, partial(test_push, ct, dir, branch, interval)).start()


def beforeexit():
    print('\n\n\n=================================\n    THANKS FOR USING AUTO-PUSH\n=================================\n\n')

def help():
    print("===================================")
    print("    AUTO-PUSH")
    print("===================================")
    print("Usage: python3 main.py [--dir] [--branch] [--commit] [--interval]")
    print("\n--dir\tis the path to the directory you want to push. Defaults to CURRENT DIRECTORY")
    print("\n--branch\tis the branch to which you want to push. Default is the result of the 'git branch' command.")
    print("\n--commit\tis a template for the commit message. Default is 'auto-commit-[uuid]")
    print("\tFor example: if --commit='auto-commit' then all the commit message will be 'auto-commit-[uuid]'.")
    print("\tNote: You can also put the uuid anywhere else in the string like so: --commit='commit-#num#-automatic'")
    print("The --commit above will be turned into 'custom-[uuid]-automatic'")
    print("\n--interval\tis the interval between pushes in minutes. Default is 5 minutes\n")
    print("Note: You can click q anytime to quit\n\n")

def listenForKeys(key):
    action = KEYS_WITH_ACTIONS.get(repr(key), None)
    if action:
        action()
