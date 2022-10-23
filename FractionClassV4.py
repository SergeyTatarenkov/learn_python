class Fraction():
    proper_fr_count = 0
    improper_fr_count = 0

    def __new__(cls, *args, **kwargs):
        print('Конструктор класса Fraction().')
        return super().__new__(cls)

    def __init__(self, numerator, denomirator):
        self.set_numerator(numerator)
        self.set_denominator(denomirator)
        Fraction.inc_fr_count(numerator < denomirator)

    def __del__(self):
        print('Деструктор класса Fraction().')

    def get_numerator(self):
        return self._numerator

    def get_denominator(self):
        return self.__denomirator

    def set_numerator(self, num):
        self._numerator = num

    def set_denominator(self, num):
        self.__denomirator = num

    @classmethod
    def inc_fr_count(cls, is_proper):
        if is_proper:
            cls.proper_fr_count += 1
        else:
            cls.improper_fr_count += 1

    def print(self):
        print('\u0332'.join(f' {self.get_numerator()} '))
        print(f' {self.get_denominator()} ')

    def reverse_frac(self):
        print('Для дроби')
        self.print()
        print('обратная дробь это')
        rev_frac = Fraction(self.get_denominator(), self.get_numerator())
        rev_frac.print()

    @staticmethod
    def get_nod(a, b):
        while a != b:
            if a > b:
                a -= b
            else:
                b -= a
        return a

    def reduce(self):
        nod = Fraction.get_nod(self.get_numerator(), self.get_denominator())
        if nod != 1:
            print('Дробь')
            self.print()
            print('после сокращения')
            self.set_numerator(self.get_numerator() // 10)
            self.set_denominator(self.get_denominator() // 10)
            self.print()
        else:
            print('Дробь')
            self.print()
            print('не может быть сокращена.')


frac1 = Fraction(1, 5)
frac2 = Fraction(15, 9)
frac2.reduce()
frac3 = Fraction(9, 7)
print(f'Правильных дробей:{Fraction.proper_fr_count}')
print(f'Неправильных дробей:{Fraction.improper_fr_count}')
