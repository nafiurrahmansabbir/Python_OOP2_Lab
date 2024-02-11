a=int(input("Enter angle 1: "))
b=int(input("Enter angle 2: "))
c=int(input("Enter angle 3: "))
if((a+b)>c) and ((a+c)>b) and ((c+b)>a):
    if a==b==c:
        print("Equilateral Triangle")
    elif a==b or b==c or c==a:
        print("lsosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle!")