import ctypes, sys
import os

_path = os.getcwd()
# FILENAME_LENGTH = len(os.path.basename(__file__))
# PATH_LENGTH = len(path)
# 
# path = path[:(PATH_LENGTH-FILENAME_LENGTH)]

print("__file__: ",__file__)
print("getcwd: ", os.getcwd())

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    cmd = [
        r'''if not exist "C:\\Program Files\auto-push" mkdir "C:\\Program Files\auto-push"''',
        f'''copy "{_path}\\auto-push.exe" "C:\\\\Program Files\\auto-push"''',
        "msg %username% Auto-Push is has been installed successfully. Final step is to add 'C:\\\\Program Files\\auto-push' to the PATH environment variable"
    ]
    
    for command in cmd:
        print("Running: ",command)
        os.system(command)
    
    input("\n\nPress Any Key To Close This...")

else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)


