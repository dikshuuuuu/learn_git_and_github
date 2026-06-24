# 1)odd loop to display  element form given list present tha odd index posditions
'''       
  
my_ in range(1,len1):
#print(i)
 ifi%2!=0 :
 print(list[i])  
      

list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for i in range(1, len(my_list),2):
    print(my_list[i])
    
 '''  

#while loop 1)

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
i = 1  

while i < len(my_list):
    print(my_list[i])
    i += 2   
 
    
 ##  2)while loop
list1=[10,20,30,40,50,60,70,80,90,100]
len1=len(list1)
index=1
while index < len1:
    print(list1[index])
    index+=2
    
#  15.	Implement a user authentication system where users need to enter their username
 #and password. If the entered username and password match the stored credentials, grant access;
 #otherwise, allow the user to try again, with a maximum of three attempts.
 
 
    
d_user = "admin"
pass1 = "admin123"

attempt=1
while attempt<=3:
   username = input("Enter username: ")
   password = input("Enter password: ")
   if username == d_user and password == pass1:
        print("Access ")
        break
   else:
        print("wrong")
        
        print(attempt,"attempt completed") 
        attempt+=1
        
##   Problem: Given a list of tasks, use a while loop alongside the .pop()
 #method to remove and print the last item of the list one by one until the list is completely empty.

tasks = ["dishes", "laundry", "groceries"]  
print("lenght:",list1)
while len(list1)>0:
    print(list1.pop())
    print("update list:",list1)
    print(len(list1))

##    
##Problem: Given a list of tasks, use a while loop alongside the .pop()
## method to remove and print the last item of the list one by one until the list is completely empty.

test="python progrming"
vowel_count=0
for ch in test:
    if ch in "aeiou":
      vowel_count +=1  
print("number of vowrls:",vowel_count) 

     
