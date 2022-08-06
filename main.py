import atexit
import sys
import os
import subprocess
import re

from methods import param_dict, colorcode, beforeexit, push, help

atexit.register(beforeexit)

""" 
The needed parameters are:
- folder -> default: _currentdir
- branch -> default: main
- commit message template -> format `message-{uuid}`
- interval
"""

args = sys.argv[1:]

""" Check if the any help is needed else parse the arguments """
if len(args) == 0 or "--help" in args:
    help()
    sys.exit(0)
else:
    print('Executing')
    params = param_dict(args)


""" Setting the DIRECTORY """
dir = os.getcwd() if "--dir" not in params.keys() else params["--dir"]

""" Check the branch """
cur_branch = "main"

try:
    cur_branch = subprocess.check_output(["git", "-C", dir, "branch"])
except Exception as e:
    print("{error}".format(error=colorcode(repr(e), "white", "bg-red")))
    sys.exit(0)

regCheck = re.search(r"(\*\s((.*){2,}))", cur_branch.decode())

cur_branch = regCheck.group(2)



branch = cur_branch if "--branch" not in params.keys() else params["--branch"]

""" Commit message template """
commit_template = "auto-commit-#num#" if "--commit" not in params.keys() else params["--commit"]

""" Interval """
interval = 5
try:
    interval = 5 if "--interval" not in params.keys() else float(params["--interval"])
except ValueError:
    print("{error}".format(error=colorcode("Given --interval is not a number", "white", "bg-red")))
    sys.exit(0)
except Exception as e:
    print(f'ERROR: {e}')
    sys.exit(0)


print('\n')

""" SET UP THE BRANCH """
try:
    subprocess.call(["git", "-C", dir, "branch", "-M", branch])
    print("--> Set Branch to {br}".format(br=colorcode(branch, "green")))
except Exception as e:
    print("{error}".format(error=colorcode(repr(e), "white", "bg-red")))
    sys.exit(0)



""" Push periodically """
push(commit_template, dir, branch, interval)




    
