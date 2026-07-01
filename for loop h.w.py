##   for lopp promind password 
'''
password="12345678"

while (password)<8:
  
    password =input("creating password:")
if len(password)<8:
    print(" Toos short")
else:
   print("password acceped")
  
   
## while loop
#2
while True:
    password =input("enter a password(8 digit):")
    
    if len (password)>=8:
    print("password accepted")
    break:
else:
     print("to short!plz tray again")   
  
## 3)
list1=[45,82,94,12,75,63]
max_score= list1[0]

for i in list1:
     
    if i>max_score:
         max_score=i
print("largest value",max_score)    
     
     
## 4)
list1=["'a','b','a','c','b','d'"]
new=[]
for i in list1:
   # print(i)
   if i not in new:
    new.append(i)    
    
print("unique  value list:",new)

## 5)
numbers=[1,2,3,4,5]
new=[]
for i in numbers:
    if i % 2!=0:
        print(i)
        sq=i**2
      
print(new)    

## 6)print multiplication table given number

num=int(input("Enter a number:"))

for i in range(2,num+1) :
  # print(i) 
  for num in range(2,i):
      if i%num==0:
          break
  else:
     print(i,"yes prime number")
      
## 7)print factorial given number
n= int(input("enter a number"))
factorial =1
for i in range(1,n+1):
    factorial*=i
    
    print("factorial=",factorial) 
    
  # #  8)print python squares all number from 1 to 10 using a for loop  
for i in range(1,11):
   square= i** 2
   print("square of", i,"=", square)
'''
## 9) print sum of all even number from  1 to 10 using a loop

sum =0
for i in range (2, 21, 2):
    sum=sum+i
print(sum of even numbers from 1 to 20 is:",sum)
 
   
      
      
 