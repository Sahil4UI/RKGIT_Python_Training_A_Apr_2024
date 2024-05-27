data = None
with open("img.jpeg","rb") as file:
    data=file.read()
    print(data)

with open("img2.jpeg","wb") as file:
    file.write(data)
