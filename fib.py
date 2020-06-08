"""
Fibonnacci series
"""
n=int(input())
a=0
b=1
if(n==0):
    print(a,end=" ")
elif(n==1):
    print(a,end=" ")
    print(b,end=" ")
elif(n<0):
    print("Enter a positive integer")
else:
    print(a,end=" ")
    print(b,end=" ")
    for i in range(n-1):
        c=a+b
        print(c,end=" ")
        a=b
        b=c
        
