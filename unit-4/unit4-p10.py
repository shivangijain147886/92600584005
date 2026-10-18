# Practical 10: File pointer operations using seek() and tell()

f = open("demo.txt", "w")
f.write("Python Programming")
f.close()

f = open("demo.txt", "r")

print("Initial position:", f.tell())
print("Read characters:", f.read(6))
print("Position after reading:", f.tell())

f.seek(0)  # Move the file pointer to the beginning
print("After seek(0):", f.tell())
print("Read again:", f.read(6))

f.close()
