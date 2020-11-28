import subprocess
import sys, os
from subprocess import CREATE_NEW_CONSOLE

if sys.platform != 'win32':
    sys.exit("This program only support Win32")

From = input("from where?")
To = input("To where?")

cpu_cores = os.cpu_count()
print("Detected {cpu_cores} CPU cores")
if cpu_cores == None:
    cpu_cores = 1

process = subprocess.Popen(
    f'cmd /K Robocopy.exe {From} {To} /e /mt:{cpu_cores}',
    creationflags=CREATE_NEW_CONSOLE)

print(f'Robocopy from {From} to {To} started')
