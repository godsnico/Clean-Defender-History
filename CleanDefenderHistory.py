import os
import subprocess
import ctypes
import sys
import time


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    print("[ERROR] Error #1 (Run Administartor)")
    sys.exit()

def print_title():
    os.system('title Windows Defender History Cleaner (WDFC) by @godsnico v1.0')
    title = """
 _____  ______ ______ ______ _   _ _____  ______ _____    _______ ____   ____  _      
|  __ \|  ____|  ____|  ____| \ | |  __ \|  ____|  __ \  |__   __/ __ \ / __ \| |     
| |  | | |__  | |__  | |__  |  \| | |  | | |__  | |__) |    | | | |  | | |  | | |     
| |  | |  __| |  __| |  __| | . ` | |  | |  __| |  _  /     | | | |  | | |  | | |     
| |__| | |____| |    | |____| |\  | |__| | |____| | \ \     | | | |__| | |__| | |____ 
|_____/|______|_|    |______|_| \_|_____/|______|_|  \_\    |_|  \____/ \____/|______|
    """
    print(title)

def loading_animation():
    animation = "|/-\\"
    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write("\r[" + animation[i % len(animation)] + "]")
        sys.stdout.flush()
    print("\r[+] Loading complete!")
    time.sleep(1)
    print("\r[-] History cleaned!") 
    time.sleep(2 )
    os.system('cls' if os.name == 'nt' else 'clear')  



print_title()
loading_animation()

create_task_cmd = [
    'schtasks', '/create', '/f', '/sc', 'onStart', 
    '/ru', 'NT AUTHORITY\\SYSTEM', '/tn', 'DWDH', 
    '/tr', 'cmd /c cd /d "C:\\ProgramData\\Microsoft\\Windows Defender\\Scans" & '
           'rd /s /q History\\Service & del /f mpenginedb.db* & '
           'schtasks /delete /f /tn DWDH'
]

subprocess.run(create_task_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

check_task_cmd = ['schtasks', '/query', '/tn', 'DWDH']
if subprocess.run(check_task_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode != 0:
    print("[ERROR] Error #2 (Error while create task, check Administartor)")
    sys.exit()

restart = input("[-] Restart now to clear Defender history (y/n)? ").lower()
if restart == 'y':
    os.system('shutdown /r /t 0')
else: 
    print("[!] Remember to reboot your PC to apply the clean!")
    time.sleep(2)
    sys.exit()