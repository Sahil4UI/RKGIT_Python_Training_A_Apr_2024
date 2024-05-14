with open("myfile.txt","r") as file:
    data = file.readlines()
    print(f"no of lines :{len(data)} ")
    str1=" ".join(data)
    withspace,withoutspace = 0,0
    withspace = len(str1)
    withoutspace = len(str1) - str1.count(" ")


