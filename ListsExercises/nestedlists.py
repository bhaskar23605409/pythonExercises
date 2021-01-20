n=[[10,20,30],[40,50,60],[70,80,90]]
print('Elemenets in row wise')
for x in n:
    print(x)

print('Elements in Matrix Wise')

for x in n:
    for y in x:
        print(y,end=' ')
    print()
