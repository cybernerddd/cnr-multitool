import os #means i wanna interact with an os features
import sys
from tkinter import W #means i want to read CLI arguments

#check if the user typed in an arg
# like for inst. python recon.py 192.168.1.1

if len(sys.argv) < 2: #If user didn’t type a second thing (like a directory), then stop the program.
    print("Usage recon.py <directory>") #tell usr how to use this tool

    sys.exit(1) # stop running the script



# read the dir paath
target = sys.argv[1] #Take the second argument the user typed, and store it in a variable.

#check if the dir exist
if not os.path.isdir(target): #If this path is NOT a real folder…
    print("Error: Directory does not exit") #Tell the user the path is fake and stop.

    sys.exit(1)

# OS detection
os_name = sys.platform #Ask Python: “Which OS am I running on?”
print(f"[os] {os_name}")

#list files in the dir
files = os.listdir(target)
#loop through the files

for f in files:
    #Take each file one by one.
    full_path = os.path.join(target, f) #Combine the folder with the filename to get the complete path.

    print(f"[FILE] {full_path}")

# now save everythong in a file
with open("recon.txt", "w") as output:
    output.write(f"[OS] {os_name}")

    for f in files:
        full_path = os.path.join(target, f)
        output.write(f"[FILE] {full_path}\n")