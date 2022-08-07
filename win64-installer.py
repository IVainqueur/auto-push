import os

cmd = [
    "if not exist \"C:\\Program Files\\auto-push\" mkdir \"C:\\Program Files\\auto-push\"",
    "copy \".\\dist\\auto-push.exe\" \"C:\\Program Files\\auto-push\""
]
for command in cmd:
    os.system(command)
