import os
f=tempfile.NamedTemporaryFile("w+b", prefix ="StevesnamePrefix",suffix=".txt")
f.write("this could be a json in string format".encode())
#this next bits seeks the start of the text to read.
f.seek(0)
print(f.read())

filename = f.name
print(filename)
f.close()
