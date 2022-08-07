import ctypes, sys
import os


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    cmd = [
        "if not exist \"C:\\Program Files\\auto-push\" mkdir \"C:\\Program Files\\auto-push\"",
        "copy \".\\dist\\auto-push.exe\" \"C:\\Program Files\\auto-push\"",
        "setx {0} \"{1}\"".format("PATH", (os.environ["PATH"] + "\"C:\\Program Files\\auto-push\""))
    ]
    for command in cmd:
        os.system(command)
    
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


