import sys
import os
import subprocess
import re

from methods import param_dict, colorcode, commit_message

""" 
The needed parameters are:
- folder -> default: _currentdir
- branch -> default: main
- commit message template -> format `message-{uuid}`
- 
"""

args = sys.argv[1:]

""" Check if the any help is needed else parse the arguments """
if len(args) == 0 or "--help" in args:
    print('Help menu')
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


""" SET UP THE BRANCH """
try:
    subprocess.check_output(["git", "-C", dir, "branch", "-M", branch])
except Exception as e:
    print("{error}".format(error=colorcode(repr(e), "white", "bg-red")))
    sys.exit(0)



# print(f'{dir} \n{branch}\n{commit_template}')


    
