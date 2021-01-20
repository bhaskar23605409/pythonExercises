#List Merging:

l1=['a','b']
l2=['c','d']
print(l1+l2)

l1.append(l2)
print(l1)

l4=['e','f','g']
l4.extend(l1)
print(l4)


x = [10, 20, 30] 
y = x*3 
print(y)

# List Comparison:


x = ["Dog", "Cat", "Rat"] 
y = ["Dog", "Cat", "Rat"] 
z = ["DOG", "CAT", "RAT"] 
print(x == y) 
print(x == z) 
print(x != z)



# Sorting 

n = [40,10,30,20] 
n.sort() 
print(n) 
n.sort(reverse = True) 
print(n)
n.sort(reverse = False) 
print(n)