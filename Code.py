from math import *
a=int(input("Give a : "))
b=int(input("Give b : "))
c=int(input("Give c : "))
D=b**2-4*a*c
RCD=sqrt(D)
if D>0:
    x1=((-b+RCD)/2+a)
    x2=((-b-RCD)/+a)
    print("x1=",x1,"x2=",x2)
elif D==0:
    x=(-b/2*a)
    print("x=",x)
else:
    print("impossible")