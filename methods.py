import re
import subprocess
import sys
from threading import Timer
from uuid import uuid4
from functools import partial


colors_with_codes = {
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
    "clear": "\x1B[0m"
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
    if color not in colors_with_codes.keys():
        return f'{text}'

    if bg not in colors_with_codes.keys():
        return f'{colors_with_codes[color]}{text}{colors_with_codes["clear"]}'
    
    return f'{colors_with_codes[color]}{colors_with_codes[bg]}{text}{colors_with_codes["clear"]}'

def commit_message(template):
    if re.search("#num#", template):
        template = re.sub("#num#", uuid4().hex, template)
    else:
        template = f'{template}-{uuid4().hex}'
    return template


def push(ct, dir, branch, interval):
    try:
        print("\n--> Pushing to {br}".format(br=colorcode(branch, "green")))
        subprocess.call(["git", "-C", dir, "add", "."], stdout=subprocess.DEVNULL)
        # print("--> Set Branch to {br}".format(br=colorcode(branch, "green")))
        subprocess.call(["git", "-C", dir, "commit", "-m", "{m}".format(m=commit_message(ct))], stdout=subprocess.DEVNULL)
        # print("--> Set Branch to {br}".format(br=colorcode(branch, "green")))
        subprocess.call(["git", "-C", dir, "push", "origin", branch], stdout=subprocess.DEVNULL)
        print("--> Pushed to {br}".format(br=colorcode(branch, "green")))
    except Exception as e:
        print("{error}".format(error=colorcode(repr(e), "white", "bg-red")))
        sys.exit(0)
    finally:
        Timer(interval*60, partial(push, ct, dir, branch, interval)).start()

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
    print("\tNote: You can also put the uuid anywhere else in the string like so: --commit='commit-%num%-automatic'")
    print("The --commit above will be turned into 'custom-[uuid]-automatic'")
    print("\n--interval\tis the interval between pushes in minutes.\n\n")