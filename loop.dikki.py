#writing a type a python to progarm first n primary numbernusing a for loop
'''number =int(input("enter your prime number"))
for i in range(1,12):
    if number % 2==0:
        print("prime number")
    else:
        print("no prime number")
        
#user_input progrm
user_input=""
while user_input !='q':
    user_input=input("enter your character(q to quiet):")
    print("your entered:",user_input)
    


adj=["red","big","testy"]  
fruits=["apple","banana","cherry"] 
for x in adj:
    for y in fruits:
        print(x,y)
        
 
    
word=["apple","banana "car","dolphpng"]
for word in words:   
#this loop in word in feathaingb word fro tha list
    print("the folloing list willprint eacha tetters of"+word)
    for letter in word:
       print(letter)
       print("")


,,,
'''

#factorial number
n=5
i=1
fact=1
while i<=n:
    fact=fact* i
    i+=1 #i=i+1
print(fact)    

#string reverse
string="vebatha"
rev=""
for char in string:
   # print(char)
    rev= char + rev
    print(rev)
if rev==  string:   
  print("palindromr string")
else:
  print("no palindromr string")  

##brack control ststemet

#1) control
for i in range(1,10):
   if i%4==0:
       break
   print(i)

#2) continue
for i in range(1,10) : 
    if i%4==0:
      continue 
print(i)

# 3)pass
for i in "hii":
  pass   #enter ,no output
 #secreat number
import random 
sec_num=random.randint(1,10)
#print (sec_num)
while True:
    user_num=int(input("enter 1 to 10 number:"))
    print(user_num)
    if sec_num==user_num:
        print("wrong")
import random
sec_num=random.randint(1,10)
#print(sec-num)
while True:
   user_num=int(input("enter a 1 to 10 number:"))
   print (user_num)
   if sec_num==user_num:
      print("yes, got it !!!")
      break
   elif sec_num>= user_num:
       print("greater is high")
   else:    
       print(("low"))
       
      

    
   
           
