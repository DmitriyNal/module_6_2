class Vehicle:
        def __init__(self, owner: str, __model: str, __engine_power: int, __color: str):
            self.owner = owner  # владелец
            self.__model = __model  # модель
            self.__engine_power = __engine_power  # мощность двигателя
            self.__color = __color  # цвет

            self.__COLOR_VARIANTS = ['red', 'green', 'blue', 'black', 'white']

        def get_model(self):  # функция возвращает модель автомобиля
            return f'Модель:{self.__model}'

        def get_horsepower(self):  # функция возвращает мощность двигателя
            return f'Мощность двигателя:{self.__engine_power}'

        def get_color(self):  # функция возвращает цвет автомобиля
            return f'Цвет:{self.__color}'

        def print_info(self):  # функция выводит информацию
            print(
                f'Модель:{self.__model},\nМощность двигателя:{self.__engine_power},\nЦвет:{self.__color},\nВладелец:{self.owner}')

        def set_color(self, new_color: str):  # функция изменяет цвет автомобиля
            if new_color.lower() in self.__COLOR_VARIANTS:
                self.__color = new_color
            else:
                print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):  # класс Sedan наследует класс Vehicle
    __PASSENGERS_LIMIT = 5#количество пассажиров в салоне





vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()

