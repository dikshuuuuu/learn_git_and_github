'''##arithmatic operators    
a=4
b=2
print("addition:",a+b) 
print("sub:",a-b)
print("multification:", a*b)
print("division:",a%b)
print("module:",a**b)
print("floor divisoin:",a/b)

'''

##assignment operator






#comparison operatatoe
x=12
y=12
print(x==y)
print(x!=y)
print(x>y)
print(x<y)
print(x<=y)
print(x>=y)

##logical operater
x=10
y=10
print(x<y and x==y) 
print(x<y or x==y)
print(not x>y)


##membership operater
string="hello"
print('o' in string)
print('c'in string)
print("e"not in string )  

##identity operater
x=10
y=10
print(x is y)    
print(x is not y)

##but
x=10
y=8

print(x&y)
print(x|y)
print(x^y)

print(bin(x),bin(y))
 #       8  4  2  1
 #x=     10 0  1

#ternary operater
a,b=10,20 
min1=a if a<b else b
print(min1) 

#if else ststment
if a<b:
    print(a)
else: 
    print(b)
#even odd number

num=4

even_odd_num="even number" if num%2==0 else"odd number"
print(even_odd_num)
 
num=3
even_odd_num="even number" if num%2==0 else"odd number"
print(even_odd_num)

# print "adult" and person based age

age=18

adult_minor="adult" if age>18 else "mine"
print(adult_minor)

age=25
adult_minor="au=dult" if age<18 else "minor"

