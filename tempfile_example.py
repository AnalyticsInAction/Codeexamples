##example code : https://colab.research.google.com/drive/17yT2RUKvNENVYZu9hq-q0s-hK7wZX6WA?usp=sharing
#no context manager is used so we will need to close manually

import tempfile
f=tempfile.NamedTemporaryFile("w+b", prefix ="StevesnamePrefix",suffix=".txt")
f.write("this could be a json in string format".encode())
#this next bits seeks the start of the text to read.
f.seek(0)
#read the context
print(f.read())

filename = f.name
print(filename)
f.close()
