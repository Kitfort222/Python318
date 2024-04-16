class Car:
    model = "model"
    year = "0000"
    name = "name"
    power = "power"
    color = "color"
    price = "price"


    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model}\nГод выпуска: {self.year}\nПроизводитель: {self.name}\n"
          f"Мощность двигателя: {self.power}\nЦвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 40)


    def input_info(self, model, year, name, power, color, price):
        self.model = model
        self.year = year
        self.name = name
        self.power = power
        self.color = color
        self.price = price


    def set_model(self, model):  # устанавливаем новое имя
        self.model = model


    def get_model(self):  # получаем имя
        return self.model


    def set_year(self, value):
        self.year = value


    def get_year(self):
        return self.year


h1 = Car()
h1.print_info()
h1.input_info("X7 M50i", "2021", "BMW", "530 л.с.", "white", "10790000")
h1.print_info()
h1.set_model("Audi")
print(h1.get_model())
h1.set_year("2022")
print(h1.get_year())

