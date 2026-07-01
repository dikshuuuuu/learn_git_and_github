###  for loop
'''
##1) 1to 10 number print 
for i in range(1,11):
    print(i)

##2)print even number 
for i in range(2,21,2):
    print(i)
 
##3)for loop number 10 to 1
for i in range(10 ,0,-1) :
    print(i)
    
##4)print even number from 2to 2
for i in range(20,1,-2):    
   print(i)
   
## 5)print tha sum of number from 1 to 10 
sum =0
for i in range(1,11): 
    sum=sum =i
print("sum=",sum)   

## 6)print multiplication table given number
num=int(input("enter a number"))

for i in range(1,11):
    print(num,"x",i,"="*1)
    
## 7)print tha factorial give number
num=int(input("enter a number:"))   
face =1
for i in range(1, num+1):
    face=face*1
    print("facetorial=",face)'''
## 8)  all number using for 1 to 10  loop
for i in range(1,11):
    print(i,"->",i*i)
    
## 9) print sum all even number 1 to 20 using for loop
sum=0
for i in range(2,21,2):
    sum=sum+1
    print("sum even number =",sum)