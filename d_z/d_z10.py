class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self.__name = new_name
        else:
            print("Имя должно быть строкой")
        self.__name = new_name

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, new_old):
        if isinstance(new_old, int):
            self.__old = new_old
        else:
            print("Возраст указать числом")
        self.__old = new_old

    @name.deleter
    def name(self):
        del self.__name


p = Person('Irina', 26)
print(p.__dict__)
p.name = "Igor"
p.old = 31
print(p.name)
print(p.old)

del p.name
p.old = 26
print(p.__dict__)
