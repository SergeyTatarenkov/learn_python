from math import sqrt


class Fraction():
    numerator = 3
    denomerator = 21

    def print(self):
        print('\u0332'.join(f' {self.numerator} '))
        print(f' {self.denomerator} ')

    def reverse_frac(self):
        print('Для дроби')
        self.print()
        print('обратная дробь это')
        rev_frac = Fraction()
        rev_frac.numerator = self.denomerator
        rev_frac.denomerator = self.numerator
        rev_frac.print()

    def reduce(self):
        a = self.numerator
        b = self.denomerator
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        if a != 1:
            print('Дробь')
            self.print()
            print('после сокращения')
            self.numerator //= a
            self.denomerator //= a
            self.print()
        else:
            print('Дробь')
            self.print()
            print('не может быть сокращена.')


'''frac = Fraction()
frac.print()
frac.reverse_frac()
frac.reduce()'''


class Vector():
    x = 2
    y = 4
    z = 6

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


vector = Vector()
vector.print()
print(f"Длина вектора {vector.lenght_vector()}")
vector.multiply(2)
print(f"Длина вектора {vector.lenght_vector()}")