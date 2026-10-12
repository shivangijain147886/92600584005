import shutil
import os

# Create a file
with open("data.txt", "w") as f:
    f.write("Hello Python")

# Copy the file
shutil.copy("data.txt", "copy.txt")
print("File copied successfully")

# Move the file
shutil.move("copy.txt", "moved.txt")
print("File moved successfully")

# Delete the file
os.remove("moved.txt")
print("File deleted successfully")
