# otning yuroladigan joylari

x1=int(input("x1: "))
y1=int(input("y1: "))
x2=int(input("x2: "))
y2=int(input("y2: "))
if abs(x1-x2)==1 and abs(y1-y2)==2:
    print("Yuroladi")
elif abs(x1-x2)==2 and abs(y1-y2)==1:
    print("Yuroladi")
else:
    print("yurolmaydi")