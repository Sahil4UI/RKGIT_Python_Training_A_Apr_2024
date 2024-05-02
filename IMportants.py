#Find the distance b/w 2 points
'''
import math
x1,x2,y1,y2 = 4,2,16,8
distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
print(distance)
'''
#@find the roots
'''
a,b,c,=1,4,6
d = b**2-4*a*c
if d==0:
    print("Roots are real and equal")
    print(f"Roots : {-b/2*a}")
elif d>0:
    print("Roots are real and unique")
    print(f"roots : {(-b+d**0.5)/(2*a)},{(-b-d**0.5)/(2*a)}")
else:
    print("Roots are Imaginary")
'''
#find the sum of digits of number
'''
x = int(input("Enter No:"))
res = 0

for i in range(len(str(x))):
    rem = x%10
    res += rem
    x //=10
    
print(res)
'''
'''
f=0
s=1
print(f"{f},{s},",end="")
for i in range(1,9):
    t=f+s
    print(t,end=",")
    f=s
    s=t
'''
#Check whether a number is prime or not
'''
x = int(input("Enter no:"))
for i in range(2,x):
    if x%i==0:
        print("Not Prime")
else:
    print("Prime")
'''
#reverse
x = int(input("Enter No:"))
res = 0

for i in range(len(str(x))):
    rem = x%10
    res = res*10+rem
    x //=10
print(res)   









