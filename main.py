import sys
import os
from methods import param_dict, colorcode

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
branch = "main" if "--branch" not in params.keys() else params["--branch"]

""" Commit message template """

print(f'{dir} {branch}')


    
