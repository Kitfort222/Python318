class Integer:
    @staticmethod
    def verify_coord(coord):
        if not isinstance(coord, int):
            raise ValueError(f"Координата {coord} должно быть целым числом")

    def __set_name__(self, owner, name):
        self.__name = "_" + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.__name]
        return getattr(instance, self.__name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        # instance.__dict__[self.__name] = value
        setattr(instance, self.__name, value)


class Order:
    price = Integer()
    res = Integer()
    # model = Integer()

    def __init__(self, model, price, res):
        self.model = model
        self.price = price
        self.res = res


p1 = Order('apple',5, 10)
print(p1.__dict__)