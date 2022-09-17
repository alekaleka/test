import numpy as np
'''
x = float(input("Enter x:"))
y = float(input("Enter y:"))
u = float
'''
#zadacha a
'''
if(x*x+y*y<=1 and x*x+y*y<=4):
    u = 0
else:
    u = x
print(u)
'''
#zadacha b
'''
if(y>=x/2 and x*x+y*y>=1):
    u = -3
else:
    u = y*y

print(u)
'''
#zadacha v
'''
if(x*x+(y-1)<=1 and 1-x*x<=y):
    u = x-y
else:
    u = y*x+7

print(u)
'''
#zadacha g
'''
if(x*x+y*y<=1 and x*x>=0.3):
    u = 0
else:
    u = x
print(u)
'''
#zadacha d
'''
if(y>=np.abs(x) and x<=y):
    u = np.sqrt(np.abs(x*x-1))
else:
    u = x+y
    
print(u)
'''
#zadacha zh

'''
if(y<=np.abs(np.e) and (np.e)**x<=y) and y<=x**2:
    u = x+y
else:
    u = x-y

print(u)
'''
#zadacha 2.1
'''
if(y<2-4*x and y<2+4*x and y>-1):
    print("Yes")
else:
    print("No")
'''
#zadacha 2.2
'''
if(y<2-4*x and y<2+4*x and y>-1):
    print("Yes")
else:
    print("No")
'''

#zadacha 2.3

x = float(input("Enter x: "))
y = float(input("Enter y: "))

if -2 <= y <= np.fabs(x) and -1 <= x <= 1:
        print("Yes")
else:
        print("No")

