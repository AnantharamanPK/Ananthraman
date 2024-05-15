x=int(input("Enter 1st number:"))
y=int(input("Enter 2nd number:"))
z=int(input("Enter 3nd number:"))

def lar(a,b,c):
    if (a>b)&(a>c):
        print(a," is greatest")
    elif (b>a)&(b>c):
        print(b," is greatest")
    else:
        print(c," is greatest")

lar(x,y,z)
