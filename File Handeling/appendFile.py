data = '''
3.Predictive Modeling
4.Data Visualization with matplotlib
'''
with open("xyz.txt","r+") as file:
    file.write(data)
    x = file.readlines()
    print(x)

