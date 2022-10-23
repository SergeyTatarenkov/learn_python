from math import sqrt


class Vector():
    start_point = (0, 0, 0)

    def __new__(cls, *args, **kwargs):
        print('Конструктор класса Vector().')
        return super().__new__(cls)

    def __init__(self, x, y, z):
        self.set_end_point(x, y, z)
        self.set_x(x - Vector.start_point[0])
        self.set_y(y - Vector.start_point[1])
        self.set_z(z - Vector.start_point[2])

    def __del__(self):
        print('Деструктор класса Vector().')

    def get_end_point(self):
        return self._end_point

    def set_end_point(self, x, y, z):
        self._end_point = (x, y, z)

    def get_x(self):
        return self.__x

    def set_x(self, x):
        self.__x = x

    def get_y(self):
        return self.__y

    def set_y(self, y):
        self.__y = y

    def get_z(self):
        return self.__z

    def set_z(self, z):
        self.__z = z

    @classmethod
    def set_start_point(cls, x, y, z):
        cls.start_point = (x, y, z)

    def print(self):
        print(f"Вектор({self.get_x()};{self.get_y()};{self.get_z()})")

    @staticmethod
    def get_length(x, y, z):
        return sqrt(x ** 2 + y ** 2 + z ** 2)

    def length_vector(self):
        length = Vector.get_length(self.get_x(), self.get_y(), self.get_z())
        return round(length, 2)

    def multiply(self, num):
        self.set_x(self.get_x() * num)
        self.set_y(self.get_y() * num)
        self.set_z(self.get_z() * num)
        print('Новый вектор')
        self.print()


v1 = Vector(4, 5, 6)
v1.print()
print(f"Длина вектора {v1.length_vector()}")
v1.multiply(2)
print(f"Длина вектора {v1.length_vector()}")
