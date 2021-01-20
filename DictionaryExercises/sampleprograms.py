word=input("Enter any word: ") 
d={} 
for x in word: 
    d[x]=d.get(x,0)+1 
for k,v in d.items(): 
    print(k,"occurred ",v," times")



n=int(input("Enter the number of students: ")) 
d={} 
for i in range(n):
    name=input("Enter Student Name: ") 
    marks=input("Enter Student Marks: ") 
    d[name]=marks 
while True:
    name=input("Enter Student Name to get Marks: ") 
    marks=d.get(name,-1)
    if marks== -1:
        print("Student Not Found")
    else:
        print("The Marks of",name,"are",marks)
    option=input("Do you want to find another student marks[Yes|No]")
    if option.lower()=="no":
        break 
print("Thanks for using our application")




#Dictionary Comprehension


squares={x:x*x for x in range(1,6)} 
print(squares) 
doubles={x:2*x for x in range(1,6)} 
print(doubles)