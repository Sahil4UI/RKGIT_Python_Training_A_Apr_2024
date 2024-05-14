file = open("myfile.txt","r")
# data = file.readline(6)
# it will read only one line
# data = file.read()
#it will read all the lines and store them
# in a string
data = file.readlines()[-1]
print(data)
file.close()