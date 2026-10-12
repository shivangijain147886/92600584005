import os
import sys

# Display current directory
print("Current Directory:", os.getcwd())

# Create a directory
os.makedirs("MyFolder", exist_ok=True)
print("Directory created")

# Create a file and write data
with open("MyFolder/data.txt", "w") as f:
    f.write("Hello Python")

print("File created")

# List files and directories
print("Files:", os.listdir("MyFolder"))

# Display Python version
print("Python Version:", sys.version)

# Display command-line arguments
print("Command Line Arguments:", sys.argv)

# Delete the file
os.remove("MyFolder/data.txt")
print("File deleted")

# Delete the directory
os.rmdir("MyFolder")
print("Directory deleted")
