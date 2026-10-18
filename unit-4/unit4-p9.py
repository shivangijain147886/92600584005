# Practical 9: Read and write data using different file modes

# Write mode: creates a file or replaces its old content
f = open("demo.txt", "w")
f.write("Hello Python")
f.close()

# Read mode: reads the file content
f = open("demo.txt", "r")
print("File content:")
print(f.read())
f.close()

# Append mode: adds new content at the end
f = open("demo.txt", "a")
f.write("\nWelcome to Python")
f.close()

# Read again to see the appended content
f = open("demo.txt", "r")
print("\nAfter appending:")
print(f.read())
f.close()
