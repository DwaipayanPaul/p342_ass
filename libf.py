# Library Module
import math
import csv
import random

# Methods for numerical integration
def midpoint(a,b,n,f):
    h=(b-a)/n
    x=[0 for i in range(n)]
    for i in range(n):
        x[i]=a+((i+1)*h)
    sum=0
    for i in range(n):
        sum+=h*f(x[i])
    return sum

def trapezoidal(a,b,n,f):
    h = (b - a) / n
    x = [0 for i in range(n+1)]
    for i in range(n+1):
        x[i] = a + (i * h)
    sum = 0
    w=1
    for i in range(n+1):
        if i==0 or i==n:
            w=1
        else: w=2
        sum += h * w * f(x[i])/2
    return(sum)

def simpsons(a,b,n,f):
    h = (b - a) / n
    x = [0 for i in range(n + 1)]
    for i in range(0,n+1,2):
        x[i] = a + (i * h)
    for i in range(1,n,2):
        x[i]=(x[i-1]+x[i+1])/2
    sum = 0
    w = 1
    for i in range(n + 1):
        if i == 0 or i == n:
            w = 1
        elif i%2==0:
            w = 2
        else: w=4
        sum += h * w * f(x[i]) / 3

    return sum

def monte_carlo(a,b,n,f):
    X=[]

    for i in range(n):
        r=random.random()
        r1=a+((b-a)*r)
        X.append(r1)
    sum,sum1 = 0.0,0.0

    for i in range(n):
        sum+=f(X[i])
        sum1+=(f(X[i]))**2

    p=((b-a)*sum)/n
    var=sum1/n-(sum/n)**2
    sd=math.sqrt(var)
    return p,sd

# For Q1)
def funcdt(func,x):    # deritive of function
    h = 0.0001
    y = (func(x + h) - func(x-h)) / (2*h)
    return y

def bracket(func,a,b):  # bracketing of the root


    for i in range(12):   # iteration limit: 12

        if func(a)*func(b)<0: # roots are on either sides of root(bracketing done)
            print("Bracketing complete: a=",a,"and b=",b)
            return a,b

        elif func(a)*func(b)>0:  # roots are on same side w.r.t.the root

            if abs(func(a))<abs(func(b)):  # need to shift a
                a-=1.5*(b-a)

            elif abs(func(a))>abs(func(b)): # need to shift b
                b=b+1.5*(b-a)

def bisecting(func,a,b):    # Bisection method
    i=0             # counter for iterations
    error=[]         # stores the error values for each iterations
    print("Bisecting method:")
    while(b-a>1E-6 and i<=100):    # iteration limit: 100 and abs error limit: 1E-6

        error.append(round((b - a), 7))  # error value gets appended in the array

        c=(a+b)/2             # midpoint of a and b
        if func(a)*func(c)<0:   #   if a and c are on either sides of root
            b=c               #  b is shifted to c
        elif func(a)*func(c)>0: # if a and c are on same sides of root
            a=c                # a is shifted to c
        else:
            print("Solution found:",c)   # if c is the root:f(c)=0
            return 0
        i+=1
    # print solution
    print("The solution lies between a=",a,"b=",b)
    return error  # return the error array

def falsi(func,a,b):      # Regular falsi method
    i=0            # counter for iterations
    error=[]       # stores the error values for each iterations
    print()
    print("Regular Falsi method:")

    x1,x2=a,b   # counters for calculating error: C_i+1-C_i
    while (abs(x2 - x1) > 1E-6 and i <= 200):   # iteration limit: 200 and abs error limit: 1E-6

        error.append(round(abs(x2 - x1), 7))     # error value gets appended in the array
        # False root c
        c = b - ((b - a) * func(b) / (func(b) - func(a)))

        if func(a) * func(c) < 0:  #   if a and c are on either sides of root
            b = c               #  b is shifted to c
        elif func(a) * func(c) > 0:   # if a and c are on same sides of root
            a = c              # a is shifted to c
        else:
            print("Solution found:", c)   # if c is the root:f(c)=0
            return 0

        if i%2==0:     # if the iteration no. is even
            x2=c       # C_2n=c
        else:
            x1=c       # else C_2n+1=c
        i += 1
    # print output
    print("The solution lies in range ",x1,"and ",x2)
    return error    # return the error array

def newton(func,x1):      # Newton-Raphson method
    i=0         # counter for iterations
    error=[]     # stores the error values for each iterations
    x2=0      # x1 and x2 are counters for calculating error: X_i+1-X_i
    print()
    print("Newton-Raphson method:")

    while(abs(x2-x1)>1E-6 and i<=200):    # iteration limit: 200 and abs error limit: 1E-6

        error.append(round(abs(x2 - x1), 7))    # error value gets appended in the array

        if i%2==0:       # if the iteration no. is even
            x2=x1-(func(x1)/funcdt(func,x1))   # X_2n=X_2n+1 -[f(X_2n)/f'(X_2n+1)]
        else:                                 # else
            x1=x2-(func(x2)/funcdt(func,x2))    # X_2n+1=X_2n -[f(X_2n+1)/f'(X_2n)]
        i+=1
    # print the solution
    print("The solution lies in range ", x2, "and", x1)
    return error    # return the error array

# To write an array in a text
def write_txt(str,er):
    with open(str, 'w', newline='') as file:  # str: the name of file
        writer = csv.writer(file)
        writer.writerow(["N", "pi"])  # The first row of the file
        for i in range(len(er)):
            writer.writerow([i + 1, er[i]])     # No of iteration in first column and absolute error in second column


# For Q2
def funct(x,a):  # function to calculate f(x) of a polynomial for a value x
                 # a is the array of co-efficients starting with the constant
    n=len(a)
    sum=0.0
    #  a[i] corresponds to the coefficient of x^i
    for i in range(n-1,-1,-1):
        sum+=a[i]*(x**i)   # stores the value of f(x)
    return sum

def functd1(x,a):  # 1st order derivative of a function (in case of polynomial)
    h=0.001
    y=(funct(x+h,a)-funct(x-h,a))/(2*h)    # f'(x)=[f(x+h)-f(x)]/2h
    return y

def functd2(x,a):  # 2nd order derivative of a function (in case of polynomial)
    h = 0.001
    y = (funct(x + h, a) + funct(x - h, a)-2*funct(x,a)) / (h*h)  # f"(x)=[f(x+h)-f(x-h)]/h^2
    return y

def deflate(sol,a):  # deflation
                     # a is the array of co-efficients starting with the constant
    n=len(a)
    q=[0 for i in range(n-1)]  # intialization of q(x)=p(x)/(x-x_o)
    q[n-2]=a[n-1]      # coefficient of x^n in p is x^n-1 in q
    # synthetic division
    for i in range(n-3,-1,-1):  # from x^n-2 in q
        q[i]=a[i+1]+(sol*q[i+1])

    return q   # final q

def solut(a,i): # to find solutions: i is the guess
                # a is the array of co-efficients starting with the constant
    n=len(a)  # n-1 is no. of roots

    if n!=2:  # when f is not of form: f(x)=x-c

        j1,j2=i,0  # counters for error: \alpha_i+1-\alpha_i
        j = i  # takes the guess for the solution
        a1=0   # a1 is for calculation of a=n/[G(+-)math.sqrt((n-1)*(nH-G^2))]
        k=1   # counter for iterations
        if funct(i,a)!=0:  # when i is not the root of f(x)

            while abs(j2-j1)>1E-6 and k<200:  # iteration limit: 200 and abs error limit: 1E-6
                # calculation G and H
                g=functd1(j,a)/funct(j,a)
                h=g**2-(functd2(j,a)/funct(j,a))
                # denominators : d1 and d2
                det1=g+math.sqrt((n-1)*(n*h-g**2))
                det2=g-math.sqrt((n-1)*(n*h-g**2))

                if abs(det1)>abs(det2):  # if absolute value of det1 is max
                    a1=n/det1          # a=n/[G(+)math.sqrt((n-1)*(nH-G^2))]
                else:
                    a1=n/det2          # a=n/[G(-)math.sqrt((n-1)*(nH-G^2))]

                if k%2==0:          # for even no. iteration
                    j1=j2-a1         # \alpha_2n+1=\alpha_2n - a
                    j=j1            # for next iteration: \alpha_2n+1
                            # else
                else:
                    j2=j1-a1        # \alpha_2n=\alpha_2n+1 - a
                    j=j2            # for next iteration: \alpha_2n
                k+=1

        # The iteration ended in even no.
        if k%2==0:
            print(j1)   # \alpha_2n+1 is the nearest solution
            # deflation and saving the new polynomial q as a(j1 is solution)
            a=deflate(j1,a)
        else:          # else
            print(j2)   # \alpha_2n is the nearest solution
            # deflation and saving the new polynomial q as a(j2 is solution)
            a = deflate(j2, a)
        # return the new polynomial array a
        return a

    else:  # when f is of form: f(x)=x-c
        if a[1]*a[0]<0 or a[1]<0:  # if eq is of form: x-c=0 or -x+c=0
            print(a[0]) # print         x=c (solution)
        else:                    # if eq is of form: -x+c=0
            print(-a[0]) # print        x=-c (solution)

        return 0


# THE LIBRARY MODULE ( with functions involving matrices)

def read_write(st):        # reading and writing matrix
    a=[]
    # Reading matrices from the files
    f1 = open(st, 'r')
    for line in f1.readlines():
        a.append([float(x) for x in line.split(',')])  # adding rows
    return a

def part_pivot(a,b):      # partial pivoting
    n=len(a)
    # initialise
    (c,d)=(0,0)
    for k in range(n-1):
        if a[k][k]==0:     # checking if the diagonal element is zero
            for r in range(k+1,n):
                if abs(a[r][k])>abs(a[k][k]):   # swapping
                    for i in range(n):
                        # swapping in matrix b
                        c = b[r][i]
                        b[r][i] = b[k][i]
                        b[k][i] = c
                        # swapping in matrix a
                        d=a[k][i]
                        a[k][i]=a[r][i]
                        a[r][i]=d


def matrix_mult(m,n):    # multiply two matrices
    l=len(m)
    r=[[ 0.0 for i in range(l) ] for j in range(l)]
    for i in range(l):
        for j in range(l):
            for k in range(l):
                r[i][j] = r[i][j] + (m[i][k] * n[k][j])
    return r

def print_mat(a):      # print a matrix
    n=len(a)
    for i in range(n):
        for j in range(n):
            print(a[i][j]," ",end="")
        print()


