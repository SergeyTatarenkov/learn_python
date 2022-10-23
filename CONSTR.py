class Car():
    car_count = 0
    def __new__(cls, *args, **kwargs):
        print("Конструктор класса Car().")
        print("Экземпляр класса Car() успешно создан.")
        return super().__new__(cls)

    def __init__(self):
        Car.car_count += 1
        print('Инициализатор класса Car().')
        print(f'Создано {Car.car_count} экземпляров класса Car().')

    def __del__(self):
        print("Деструктор. Объект удален.")


new_car = Car()
new_car1 = Car()
new_car2 = Car()