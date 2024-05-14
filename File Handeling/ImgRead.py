data = None
with open("Python-Symbol.png","rb") as file:
    data = file.read()
    print(data)

with open("newfile.png","wb") as file:
    file.write(data)
