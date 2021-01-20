class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def getCarInfo(self):
        print('Car Name: ',self.name)
        print('Car Model: ',self.model)
        print("Car Color: ",self.color)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def getPerson(self):
        print('Name :',self.name)
        print('Age : ',self.age)
class Employee(Person):
    def __init__(self,ename,eage,eid,ecpy,car):
        super().__init__(ename,eage)
        self.eid=eid
        self.ecpy=ecpy
        self.car=car
    def getEmp(self):
        print("The Emp name: ",self.name)
        print("The Emp age:",self.age)
        print("The Emp id: ",self.eid)
        print("The Emp ecpy: ",self.ecpy)
        self.car.getCarInfo()
c=Car("Toyota",2.5,"Grey")
e=Employee('Durga',25,1234,'Ibm',c)
e.getPerson()
e.getEmp()