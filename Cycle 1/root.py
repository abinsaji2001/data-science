import math
a=int(input("enter the coeficient of a:"))
b=int(input("enter the coeficient of b:"))
c=int(input("enter the coeficient of c:"))
d=b*b-4*a*c
f=2*a
if d<0:
    print("no real roots")
else:
    r1=(-b+math.sqrt(d))/f
    r2=(-b-math.sqrt(d))/f
    print("the first root",round(r1,2))
    print("the second root", round(r2,2))