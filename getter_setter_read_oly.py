class User():
    def __init__(self, name, age, money):
        self._name=name
        self._age= age
        self.__money= money
    
    # getter without setter is read only attribute
    @property
    def age(self):
        return self._age

    # def salary(self):
    #     return self.__money
    
    # getter without setter is read only attribute
    @property
    def salary(self):
        return self.__money
    

    @salary.setter
    def salary(self, value):
        if value < 0:
            return "can not add salary"
        self.__money+=value
anis= User("anis", 23, 52300)
# print(anis.__money)
print(anis.age)
# print(anis.salary())

print(anis.salary)
anis.salary=5000
print(anis.salary)
