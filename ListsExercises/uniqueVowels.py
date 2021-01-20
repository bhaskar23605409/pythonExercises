vowels=['a','e','i','o','u']
inputWord=input("Enter the word: \n")
output=[]
for i in inputWord:
    if i in vowels:
        if i not in output:
            output.append(i)
print(output)