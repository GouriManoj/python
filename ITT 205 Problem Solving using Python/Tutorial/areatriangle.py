
a=float(input("ENTER SIDE 1"))
b=float(input("Enter side 2"))
c=float(input("Enter side 3"))
s = (a + b + c) / 2
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is %0.2f' %area)
