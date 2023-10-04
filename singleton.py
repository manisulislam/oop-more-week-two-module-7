class Singleton:
    __instance= None
    def __init__(self):
        if Singleton.__instance is None:
            Singleton.__instance=self
        else:
            raise Exception("instances already exists")
    @staticmethod
    def get_instance():
        if Singleton.__instance is None:
            Singleton()
        return Singleton.__instance
first= Singleton.get_instance()
second= Singleton.get_instance()
third = Singleton.get_instance()
print(first)
print(second)
print(third)
last = Singleton()