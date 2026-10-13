a=int(input("enter the value of a"))
b=int(input("enter the value of b"))
c=int(input("enter the value of c"))
##check which number is greater##
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
    print("b is greater")
elif c>a and c>b:
    print("c is greater")
elif a==b and b==c and c==a:
    print("a,b,c are same")
else:
    print("invalid number")