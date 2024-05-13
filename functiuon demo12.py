#functions
'''
def f1():
    print("F1 caLLED")

    def f2():
        print("F2 called")

    def f3():
        print("F3 called")

    return f2,f3

f3=f1()[1]
f3()
'''
#named arguments
'''
def f1(x,y=2):
    print(x,y)

f1(5)
'''
# *args - special argument
'''
def f1(x,*args):
    print(x,args)

f1(12,23,345,456,657,67,56,45,3,43,4,3)
'''
#keyworded arguments
'''
def Student(name,dob,**kwargs):
    print(name,dob,kwargs)

Student("abhishek","05-05-2000",contact="9876543210",fathers="mukesh")

'''



"""
paise = [1,2,3,4,500,345,235,90345]
'''
def Rupee(x):
    return x/100
'''
Rupee = lambda x : x/100
print(list(map(Rupee,paise)))
'''
for i in paise:
    print(Rupee(i))
'''
"""
x = 1,2,3,4,5,6,7,8,9,10
'''
def f1(a):
    if a%2==0:
        return True
    else:
        return False
'''
'''
f1 = lambda a : True if(a%2==0) else False
print(list(filter(f1,x)))
'''

def f1(x):
    #base case
    if x=="":
        return 0
    
    return 1+f1(x[1:])

res = f1("python")
print(res)










































