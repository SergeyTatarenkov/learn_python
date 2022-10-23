from math import sqrt


class Vector():
    start_point = (2, 3, 7)

    def set(self, x, y, z):
        self.end_point = (x, y, z)
        self.x = x - Vector.start_point[0]
        self.y = x - Vector.start_point[1]
        self.z = x - Vector.start_point[2]

    def print(self):
        print(f"Вектор({self.x};{self.y};{self.z})")

    def lenght_vector(self):
        lenght = sqrt(self.x ** 2 + self.z ** 2 + self.z ** 2)
        return round(lenght, 2)

    def multiply(self, num):
        self.x *= num
        self.y *= num
        self.z *= num
        print('Новый вектор')
        self.print()


v1 = Vector()
v1.set(4, 5, 6)
v1.print()
print(f"Длина вектора {v1.lenght_vector()}")
v1.multiply(2)
print(f"Длина вектора {v1.lenght_vector()}")
