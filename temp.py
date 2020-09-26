import cmath
a = float(input("Enter value of a: "))
b = float(input("Enter value of b : "))
c = float(input("Enter value of c: "))
d=((b**2)-(4*a*c))
root1=(-b-cmath.sqrt(d))/(2*a)
root2=(-b+cmath.sqrt(d))/(2*a)
print("The roots are :" )
print(root1)
print(root2)





