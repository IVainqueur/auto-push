import sys
import os
from methods import param_dict

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
if "--dir" in params.keys():
    dir = params["--dir"]
else:
    dir = os.getcwd()


    
