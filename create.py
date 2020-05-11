import os
import sys
from const import const, info
import subprocess
#nt 

parent = const["parent"]

def add_folder(name):
    if name not in os.listdir(parent):
        file_path = parent + '/' + name.strip()
        os.mkdir(file_path)
        print(file_path + ' created')
        print("....")
        for folder in os.listdir(parent):
            print("> " + folder)
    else:
        print("--Folder already exsist--")

def list_note():
    for i in os.listdir(parent):
        print("--" + i)
        for x in os.listdir(parent + "/" +i):
            print("     " + x[:-4])

def open_folder(folder):
    if folder in os.listdir(parent):
        folder_path = parent + "/" + folder
        os.system(f"cd {folder_path} && subl .")
    else:
        print("❌No such Folder present❌")

def add_note_folder(folder, name):
    if folder in os.listdir(parent):
        folder_path = parent + '/' + folder
        os.system(f"cd {folder_path} && subl {name}")
    else:
        print("❌No such Folder present❌")

if __name__ == "__main__":

    cmd = sys.argv
    if cmd[1] == "n":
        note = parent + "/General/" + cmd[2].strip() + ".txt"
        with open(note, 'w') as fp:
            pass
        os.system(f"subl {note}")
    
    if cmd[1] == "a":
        add_folder(cmd[2])

    if cmd[1] == "ls":
        list_note()

    if cmd[1] == "o":
        try:
            open_folder(cmd[2])
        except IndexError:
            print("--Pleas enter a Folder name--")
            for folder in os.listdir(parent):
                print("> " + folder)
    if cmd[1] == "--help":
        print(info)
