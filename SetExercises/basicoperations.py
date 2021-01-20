#add
s={10,20,30} 
s.add(40) 
print(s)

#update
s={10,20,30} 
l=[40,50,60,10] 
s.update(l,range(5)) 
print(s)

#pop(),dicard(),remove(),clear()

s = {10, 20, 30} 
s.discard(10)
s.pop()
s.remove(30)
s.clear()


#Mathematical Opeartion on Set

s1={10,20,30,40}
s2={50,10,20}
print(s1|s2)
print(s1&s2)
print(s1-s2)


#Set Comprehension 

s = {2**x for x in range(2,10,2)} 
print(s)

s = {x*x for x in range(5)} 
print (s)