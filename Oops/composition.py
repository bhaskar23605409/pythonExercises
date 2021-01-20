class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def info(self):
        print('Car Name: ',self.name)
        print("Car Model: ",self.model)
        print("Car Color: ",self.color)
class Employee:
    def __init__(self,ename,eid,car):
        self.ename=ename
        self.eid=eid
        self.car=car
    def display(self):
        print("Emp Name: ",self.ename)
        print("Emp Id: ",self.eid)
        print("Car Info: ")
        self.car.info()
c=Car('Innova',2.5,"Grey")
e=Employee("Durga",1234,c)
e.display()