import os

# Get Current working directory
print(os.getcwd())

# List Files and Folders
files=os.listdir()
print(files)

# List python file
for file in os.listdir():
  if file.endswith(".py"):
      print(file)

# create Directory
os.mkdir("demo")
os.mkdir("demo/images")

# create file
with open("test.txt", "w") as file:
    pass

# create multiple directory
for i in range(1,4):
   os.mkdir(f"folder{i}")


# Rename directory & file
os.rename("folder3","folder4")

# Remove  directory & file
os.remove("test.txt")
os.rmdir("folder1")
os.removedirs("demo/images")   #remove nested empty directory
 
# check file exist
if os.path.exists("os.py"):
 print("exist")
else:
 print("not exist")

# Join Paths Properly
path=os.path.join("folder2","file")
print(path)

# Get size of file in byte
size=os.path.getsize("ospractice.py")
print(size)


# separate filename and extension
file="ospractice.py"
name,ext=os.path.splitext(file)
print("filename",name)
print("Extension",ext)


# Get filename and directory name
filepath=("/home/asus/learnpython/learnubuntu/osprogram.py")
print(os.path.basename(filepath))
print(os.path.dirname(filepath))


# Walk directories
for root,dirs,files in os.walk("."):
 print("Root",root)
 print("Dirs",dirs)
 print("Files",files)
