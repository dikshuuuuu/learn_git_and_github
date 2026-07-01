##zip()
'''
names=["diksha","sakshi","savi"]
scores=[90,60,80]

for name,score in zip(names,scores):
   print(f"{name}:{score}")
          
          
names=["diksha","sakshi","savi"] 
scores=[90,60,80]  
grades=["a","b","c"]  
for name,score,grade in zip(names,scores,grades):
   print(f"{name}: Score{score},Grade{grade}")  

 ##unzip 
names=["diksha","sakshi","savi"] 
scores=[90,60,80] 

zipped=zip(names,scores) 
unzipped_names,unzipped_scores=zip(*zipped)  

print(unzipped_names) #('diksha','sakshi','savi')  
print(unzipped_scores) #('90','60','80')

##
from itertools import zip_longest 
                
 
##define two list  different lenthas
list1=[1,2,3,4]
list2=['a','b']

#used a zip longest to pair up element witha a default valu
for num, letter in zip_longest(list1,list2,fillvalue='N/A'):
    print(f"number:{num},letter:{letter}")
    
##star payyern
##left side
for i in range(6):
    print("*"*i)
    
for i in range(6,0,-1):   
    print("*"*i)
    
##rihgt side  
for i in range(0,6):
    print(" "*(6-i),"*"*i)
   
for i in range(6,0,-1):
    print(" "*(6-i),"*"*i)    
 
##star 
for i in range(6):
    print("*"*i) 
    
for i in range(6,0,1) : 
    print(" "*i)

 ##
rows=4
## upper half
for i in range (1,rows + 1):
    print(" " *(rows -i)+ "*" * i)
    
## lower half
for i in range(rows -1 , 0,-1):
    print(" " * (rows - i)+ "* " * i)
 
rows = 4

# Upper 
for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

# Lower 
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)

##
rows=8
for i in range(1, rows +1):
   print(" "*(rows-i)+ "*" * i)
 
for i in range(rows -1,0,-1):
    print(" " * (rows - i)+"*"*i)
 
 ''' 
# triangle shape
for i in range(6): 
    print(" " *(6-i)+ "*"*(2*i+1))

for i in range(6,-1,-1):
    print(" "*(6-i)+"*"*(2*i+1))
  