import libf

e=2.718281828459045
f=lambda x: e**(-x**2)

print("For error of 0.001")
print()

print("Midpoint method: N=10")

l1=libf.midpoint(0,1,10,f)

print(l1)

print()
print("Trapezoidal Method: N=13")
t1=libf.trapezoidal(0,1,13,f)

print(t1)
print()
print("Simpsons Method: N=4")
s1=libf.simpsons(0,1,4,f)

print(s1)
