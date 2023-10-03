class Person:
    def __init__(self, name, age, height,weight) -> None:
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
    def eat(self):
        print("vat mangso roti kai")
    def exercise(self):
        raise NotImplementedError
class Cricketer(Person):
    def __init__(self, name, age, height, weight, team) -> None:
        self.team= team
        super().__init__(name, age, height, weight)
    def eat(self):
        print("vegetables")

    def exercise(self):
        print("gym koro gia")

    def __add__(self, other):
        return self.age+other.age
    def __mul__(self, other):
        return self.weight * other.weight
    def __len__(self):
        return self.height
    def __gt__(self, other):
        return self.age> other.age

sakib= Cricketer("sakib",30,5,65,"bd")
sakib.eat()
sakib.exercise()
mushi= Cricketer("mushi",35,6,96,"bd")


# plus overloading
print(45+65)
print("sakib"+ "anis")
print([45,20]+[12,56,74,85,96])     
print(sakib*mushi) 
print(len(sakib))
print(sakib>mushi)