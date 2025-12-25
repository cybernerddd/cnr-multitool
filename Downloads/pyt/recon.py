# # import os

# # #print(os.getcwd())
# # #os.listdir()

# # #os.mkdir("Cybernerddd")
# # #print(os.getcwd())
# # os.chdir("Cybernerddd")


# # with open("hacking.txt", "w") as f:
# #     f.write("Hacking in progress...")

# # os.remove("hacking.txt")

# # os.system("ipconfig")
# # os.system("ping google.com")

# #sys
# import sys

# # print("Argument: ", sys.argv)

# # if len(sys.argv) < 2:
# #     print("Usage: python loader.py <name>")

# #     sys.exit(1)

# # name = sys.argv[1]
# # print("Hello,", name)


# print("Filename:", sys.argv[0])

# if len(sys.argv) > 1:
#     print("First argument:", sys.argv[1])
# else:
#     print("No argument provided")

# #plateform detection, so u know which youre working with.

# # if sys.platform.startswith("win"):
# #     print("Runnning on Windows")

# # elif sys.platform.startswith("linux"):
# #     print("Runnin on Linux")

# # print(sys.path)




# # print("Platform:", sys.platform)

# # if len(sys.argv) > 1:
# #     print("Mode:", sys.argv[1])
# # else:
# #     print("No mode selected")

# import subprocess

# subprocess.run("arp -a")


# result = subprocess.run("ipconfig", capture_output=True, text=True)

# print("STDOUT:")
# print(result.stdout)

# print("STDERR:")
# print(result.stderr)


# subprocess.run("dir", shell=True)

# import subprocess

# process = subprocess.Popen(
#     ["ping", "google.com"],
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     text=True
# )

# for line in process.stdout:
#     print("LIVE →", line.strip())

# import subprocess

# cmd = "arp -a"

# process = subprocess.Popen(
#     cmd,
#     shell=True,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     text=True
# )

# for line in process.stdout:
#     print("ARP →", line.strip())

# import os
# import subprocess
# cmd = "ipconfig"

# process = subprocess.Popen(
#    cmd,
#     shell=True,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     text=True
# )

# for line in process.stdout:
#     print("IPCONFIG →", line.strip())

# p1 = subprocess.Popen("ipconfig", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
# p2 = subprocess.Popen("findstr IPv4", shell=True, stdin=p1.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

# output = p2.stdout.read()
# print(output) # this basically does "ipconfig | findstr IPv4"


# import subprocess

# while True:
#     cmd = input("Enter command (or 'exit' to quit): ")

#     if cmd.lower() == 'exit':
#         break

#     process = subprocess.Popen(
#         cmd,
#         shell=True,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         text=True
#     )

#     stdout, stderr = process.communicate()

#     if stdout:
#         print("Output:\n", stdout)
#     if stderr:
#         print("Error:\n", stderr)

# from pathlib import Path

# base = Path.cwd()
# print("Base:", base)

# logs = base / "demo_logs"
# logs.mkdir(exist_ok=True)
# print("Created directory:", logs)

# file = logs / "test.txt"
# file.write_text("Hello Cybernerddd\n")
# print("File created:", file)

# content = file.read_text()
# print("Content:", content)

# import os
# from pathlib import Path

# base = Path.cwd()
# folder_name = input("Enter folder name: ")
# folder_loc = base / folder_name

# if folder_loc.exists():
#     print("Folder already exists.")

# else:
#     folder_loc.mkdir()
#     print("Folder created at:", folder_loc)


# file_name = input("Enter file name: ")
# file_path = os.path.join(folder_path, file_name + ".txt")

# content = input("Enter content to write to the file: ")
# with open(file_path, "w") as file:
#     file.write(content)
#     print("File created at:", file_path)


# from pathlib import Path

# path = Path.cwd()
# print("Base: ", path)

# folder_name = input("Enter folder name: ")
# folder_path = path / folder_name
# if folder_path.exists():
#     print("Folder already exists: ", folder_path)
# else:
#     folder_path.mkdir()
#     print("Folder Created at: ", folder_path)

# file_name = input("Enter file name: ")
# file_path = folder_path / f"{file_name}.txt"

# content = input("Input file content here: ")
# file_path.write_text(content)
# print("File created at: ", file_path)

# from pathlib import Path

# path = Path.cwd()
# for i in path.rglob("*"): #recursive globbing, finds all files and folders in the current directory and subdirectories.
#     if i.is_file():
#         print("[FILE]")
#         print("Name: ", i.name)
#         print("Extension: ", i.suffix)
#         print("Size: ", i.stat().st_size, "bytes")
#         print("Absolute Path: ", i.resolve())
#         print("Parent: ", i.parent)
    
    
    
    
#     elif i.is_dir():
#         print("[FOLDER]")
#         print("Folder Name: ", i.name)
#         print("Absolute Path: ", i.resolve())
#         print("Parent: ", i.parent)
    

# from pathlib import Path
# import os
# import subprocess

# print("=== SYSTEM RECON ===")

# # 1. Current path
# current = Path.cwd()
# print("Current directory:", current)

# #2. list folders
# for item in current.rglob("*"):
#     folder = item.is_dir()
#     if folder:
#         print("FOLDER:", item.resolve())

# #3. print os name
# print("\n=== OS INFORMATION ===")
# os_name = os.name
# if os_name == "nt":
#     print("Operating System: Windows\n")
# elif os_name == "posix":
#     print("Operating System: Unix/Linux/Mac\n")
# else:
#     print("Operating System: Unknown\n")


# #4. ipconfig/ifconfig
# cmd = "ipconfig" if os_name == "nt" else "ifconfig"

# process = subprocess.Popen(
#     cmd,
#     shell=True,
#     stdout=subprocess.PIPE,
#     stderr=subprocess.PIPE,
#     text=True
# )

# stdout, stderr = process.communicate()
# print("=== NETWORK CONFIGURATION ===")
# print(stdout)


# from pathlib import Path
# import os
# import subprocess

# while True:
#     cmd = input("Enter command or ('exit') to quit: ")

#     if cmd.lower() == "exit":
#         break

#     process = subprocess.Popen(
#         cmd,
#         shell=True,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         text=True
#     )

#     stdout, stderr = process.communicate()

#     if stdout:
#         print("[RESULTS]\n")
#         print(stdout)
#     if stderr:
#         print("Error:\n", stderr)



# while True:
#     cmd = input("Enter command (or 'exit' to quit): ")

#     if cmd.lower() == 'exit':
#         break

#     process = subprocess.Popen(
#         cmd,
#         shell=True,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         text=True
#     )

#     stdout, stderr = process.communicate()

#     if stdout:
#         print("Output:\n", stdout)
#     if stderr:
#         print("Error:\n", stderr)



# import os

# print(os.environ)
# #how to read env variables username, userprofile, path, temp
# print("USERNAME: ", os.environ.get("USERNAME"))
# print("USERPROFILE: ", os.environ.get("USERPROFILE"))
# print("PATH: ", os.environ.get("PATH"))
# print("TEMP: ", os.environ.get("TEMP"))

# os.environ["MY_VAR"] = "Cybernerddd was here"

# print(os.environ["MY_VAR"])

# os.environ["HACKER_NAME"] = "Cybernerddd"
# print(os.environ["HACKER_NAME"])

# os.environ["PAYLOAD"] = "rm -rf /"
# print(os.environ["PAYLOAD"])

import os
import subprocess

# env = os.environ.copy()
# env["HACK_ENV"] = "ACTIVE"
# env["TOKEN"] = "12345-abcde"

# process = subprocess.Popen(
#     "set",
#     shell=True,
#     env=env,
#     stdout=subprocess.PIPE,
#     text=True

# )

# print(process.stdout.read())

# import subprocess

# subprocess.run('setx CYBER_PAYLOAD "C:\\Users\\Public\\payload.exe"', shell=True)
  # create persistent environment variable For Windows


import winreg #windows registry editing

# reg = winreg.ConnectRegistry(None, winreg.HKEY_CURRENT_USER) #connect to the current user registry hive
# key = winreg.OpenKey(reg, r"Environment", 0, winreg.KEY_SET_VALUE) #open the Environment key with permission to set values
# winreg.SetValueEx(key, "CYBER_REG", 0, winreg.REG_SZ, "http://127.0.0.1:8080") #set a new string value named CYBER_REG with the specified URL
# winreg.CloseKey(key) #close the registry key

import subprocess

# result = subprocess.run("whoami", capture_output=True, text=True)
# user = result.stdout.strip()

# print("Current user:", user)
# subprocess.run(["ping", "google.com"])

# cmd = input("Enter command to execute: ")
# result = subprocess.run(cmd, capture_output=True, text=True)

# print("stdout:", result.stdout.strip())
# print("stderr:", result.stderr.strip())


# process = subprocess.Popen(
#     "calc.exe",
#     shell=True,
#     stdout=subprocess.DEVNULL, #running command silently
#     stderr=subprocess.PIPE, # capture errors silently
#     text=True
# )

# # bg process running
# subprocess.Popen("notepad.exe", shell=True) #launch notepad in background
# print("Notepad launched in background")


import subprocess

# while True:
#     cmd = input("\nNerdddShell> ")

#     if cmd.lower() == "exit":
#         break

#     process = subprocess.Popen(
#         cmd,
#         shell=True,
#         stdout=subprocess.PIPE,
#         stderr=subprocess.PIPE,
#         text=True
#     )

#     stdout, stderr = process.communicate()

#     if stdout:
#         print("\n=== Command Output ===\n")
#         for line in stdout.splitlines():
#             print(line.strip())

#     if stderr:
#         print("\n=== Command Errors ===\n")
#         for line in stderr.splitlines():
#             print(line.strip())
        


import ctypes 
SW_HIDE = 0 #constant to hide window

#hide python console window
ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), SW_HIDE) #hide the console window

subprocess.Popen(
    "ipconfig",
    shell=True,
    creationflags=subprocess.CREATE_NO_WINDOW #run without window

)

