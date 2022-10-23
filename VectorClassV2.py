from math import sqrt


class Vector():
    start_point = (0, 0, 0)

    @classmethod
    def set_start_point(cls, x, y, z):
        cls.start_point = (x, y, z)

    def set(self, x, y, z):
        self.end_point = (x, y, z)
        self.x = x - Vector.start_point[0]
        self.y = y - Vector.start_point[1]
        self.z = z - Vector.start_point[2]

    def print(self):
        print(f"Вектор({self.x};{self.y};{self.z})")

    @staticmethod
    def get_length(x, y, z):
        return sqrt(x ** 2 + y ** 2 + z ** 2)

    def length_vector(self):
        length = Vector.get_length(self.x, self.y, self.z)
        return round(length, 2)

    def multiply(self, num):
        self.x *= num
        self.y *= num
        self.z *= num
        print('Новый вектор')
        self.print()


v1 = Vector()
v1.set(4, 5, 6)
v1.print()
print(f"Длина вектора {v1.length_vector()}")
v1.multiply(2)
print(f"Длина вектора {v1.length_vector()}")
