#  for loop

name="savi"
for i in name:
    print(i,end="")
    
#example:iterating over a tuple: 
colors=("red","pink","black",) 
for j in colors: 
    print(j)
    
#iterating over a list
li=["java","python","c"]
for x in li:
    print(x)
    
#set
set1={1,2,3,4,}
for j in set1:
    print(j) 
    
#dict
dict1={
     "name":"diksha",
     "marks":"50",
     "roll no":"10"}
print(dict1.items()) 
for i,j in dict1.items(): 
    print(i,j)
#count
a="hii,i am robot"
count=0 
for char in a:
    print(char)
    count+=1 
#count=count+1
    print(count) 
#students marks
students_marks={
"pooja":50,
"diksha":80,
"shalu":40,
"diksha":60}
for name,marks in students_marks.items():    
    print (name,marks)
    if marks>40:
        print(name,"-pass")
    else:    
    print(name,"-fail")
    

    

    