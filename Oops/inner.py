class Outer:
    def __init__(self):
        print("Outer Class")
    class Inner:
        def __init__(self):
            print("Inner Class")
        def m1(self):
            print("Inner Method Created")
Outer().Inner().m1()