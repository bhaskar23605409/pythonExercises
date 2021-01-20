class S:
    def __init__(self,marks):
        self.marks=marks

    def __add__(self,other):
        return S(self.marks+other.marks)

    def __gt__(self,other):
        return self.marks>other.marks 
    def __str__(self):
       return "The Number of Pages :{} ".format(self.marks)

s1=S(70)
s2=S(75)
s3=S(100)
print(s1+s2+s3)
print(s1>s2)