def greet(name):
    print("hello",name)
name=input()    
greet(name)    

def abc(a,b):
    sum=0
    for i in range(a,b+1):
        sum=sum+i
    return sum 
abc(5,10)

def xyz(a,b):
    even=0
    for i in range(a,b+1):
        if i%2==0:
            even+=i
    return even 
xyz(5,10)

def cde(a,b):
    odd=0
    for i in range(a,b+1):
        if i%2!=0:
            odd+=i
    return odd
cde(5,10) 

def factorial(a):
    fact=1
    if a<0:
        print(a,"is a neagtive number")
    elif a==0 or a==1:
        print(a,"is 1 ")
    else:
        for i in range(1,a+1):
            fact*=i
        return fact
factorial(5)

def num(n):
    if n>1:
        for i in range(2,n):
           if n%i==0:
               print("not a prime number")
               break
           else:
               print("prime number")
    else:
        print("not prime")
num(8)

def number(a):
    if a>0 and a%2==0:
        print(a,"postive and even")
    elif a>0 and a%2!=0:
        print(a,"postive and odd")
    elif a<0:
        print(a,"neagtive")
    else:
        print(a,"0")
number(5)

def fib(n):
    a=0
    b=1
    for i in range(0,n):
        print(a,end=" ")
        a,b=b,a+b
fib(5)

def word(s):
    if s==s[::-1]:
        print("palindrome")
    else:
        print("not palindrome")
word("amma")  

def HCF(a,b):
    while b:
        a,b=b,a%b
    return a 
HCF(36,60)