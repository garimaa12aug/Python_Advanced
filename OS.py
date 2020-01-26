import os
print(dir(os)) #gives all function possible within os module
print(os.getcwd()) #gives the current working directory
os.chdir("/home") #to change the currentr working directory to home
print(os.getcwd())
os.chdir("/home/garima/Desktop/MY_WORK/Python/Advanced")
f = open("OS_Module.py")
print(os.listdir()) #list all directories or files/folder under current working directotory
print(os.listdir("/home")) #list directories in home
os.mkdir("hello") #make a folder named hello inside current working directory
os.makedirs("world/new") #make multiple directories first would be world then inside world new named folder will be created
os.rename("OS_Module.py","OS.py") #rename a file
print(os.path.join("/home","/MY_WORK")) #joins two path
print(os.path.exists("/home")) #tells if the path exist or not
