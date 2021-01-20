class Student:
    def setMarks(self,marks):
        self.marks=marks
    def setName(self,name):
        self.name=name
    def getMarks(self):
        return self.marks
    def getName(self):
        return self.name




st=[]

for i in range(2):
    s=Student()
    name=eval(input("Enter Name: "))
    marks=eval(input("Enter Marks: "))
    s.setName(name)
    s.setMarks(marks)
    st.append(s)

for kk in st:
    print(kk.getName(),' ',kk.getMarks())

