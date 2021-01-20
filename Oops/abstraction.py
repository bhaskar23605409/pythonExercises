from abc import *
class CollegeAutomation(ABC): 
    @abstractmethod
    def m1(self): pass
    @abstractmethod
    def m2(self): pass
    @abstractmethod 
    def m3(self): pass 
class AbsCls(CollegeAutomation):
    def m1(self):
        print('m1 method implementation')
    def m2(self):
        print('m2 method implementation') 
 
class ConcreteCls(AbsCls):
    def m3(self):
        print('m3 method implemnentation')
c=ConcreteCls() 
c.m1()  
c.m2()
c.m3()