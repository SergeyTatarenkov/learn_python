class Fraction():
    proper_fr_count = 0
    improper_fr_count = 0

    def __new__(cls, *args, **kwargs):
        print('Конструктор класса Fraction().')
        return super().__new__(cls)

    def __init__(self, numerator, denomerator):
        self.numerator = numerator
        self.denomerator = denomerator
        Fraction.inc_fr_count(numerator < denomerator)

    def __del__(self):
        print('Деструктор класса Fraction().')

    @classmethod
    def inc_fr_count(cls, is_proper):
        if is_proper:
            cls.proper_fr_count += 1
        else:
            cls.improper_fr_count += 1

    '''def set(self, numerator, denomerator):
        self.numerator = numerator
        self.denomerator = denomerator
        Fraction.inc_fr_count(numerator < denomerator)'''

    def print(self):
        print('\u0332'.join(f' {self.numerator} '))
        print(f' {self.denomerator} ')

    def reverse_frac(self):
        print('Для дроби')
        self.print()
        print('обратная дробь это')
        rev_frac = Fraction(self.numerator, self.denomerator)
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
        nod = Fraction.get_nod(self.numerator, self.denomerator)
        if nod != 1:
            print('Дробь')
            self.print()
            print('после сокращения')
            self.numerator //= nod
            self.denomerator //= nod
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
