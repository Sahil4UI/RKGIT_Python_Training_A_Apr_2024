data = [1,2,3,4,5,6,7,8,9,10]
"""
'''
def f1(x):
    if x%2==0:
        return True
    else:
        return False
'''
f1 = lambda x : True if (x%2==0) else False
print(list(filter(f1,data)))
"""
'''
def f1(string):
    if string=="":
        return 0

    return 1+ f1(string[1:])

res = f1("Hello Python")
print(res)
'''
'''
def pattern(x):
    if x>5:
        return

    print("*"*x)
    pattern(x+1) 
pattern(1)
'''
#*args & **kwargs
'''
def f1(x,*y):
    print(x,y)

f1(12,34,456,457,568)
'''
'''
def f1(x,y=13):
    print(x,y)
f1(12)
'''
'''
#**kwargs - keyworded argument
def f1(roll,name,div,**other_details):
    print(roll,name,div,other_details)

f1(101,"Abhishek",10,parents="rohit",contact="9876543210")

#Tic tac Toe using Python
'''
win_comb = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
def Grid(x):
    for i in range(len(x)):
        if i in(2,5,8):
            print(x[i])
            print("---------")
        else:
            print(x[i],end=" | ")
            
def playerMove(choice,pos,x):
    x[pos-1]=choice
    Grid(x)
    return Wins(choice,x)
    
def Wins(choice,x):
    for i in win_comb:
        if x[i[0]]==choice and x[i[1]]==choice and x[i[2]]==choice:
            return choice
    return 0
x = [i for i in range(1,10)]
Grid(x)
user_choice = input("Enter Choice X/0 : ").upper()
cpu_choice = "0" if(user_choice=="X") else "X"
while True:
    pos = int(input("Enter Pos (1-9):"))
    res = playerMove(user_choice,pos,x)
    print(res)
    if res == user_choice:
        print(res," is winner")
        break
    









































































































