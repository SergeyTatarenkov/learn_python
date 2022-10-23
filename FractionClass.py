class Fraction():
    proper_fr_count = 0
    improper_fr_count = 0

    def set(self, numerator, denomerator):
        self.numerator = numerator
        self.denomerator = denomerator
        if numerator < denomerator:
            Fraction.proper_fr_count += 1
        else:
            Fraction.improper_fr_count += 1


    def print(self):
        print('\u0332'.join(f' {self.numerator} '))
        print(f' {self.denomerator} ')

    def reverse_frac(self):
        print('Для дроби')
        self.print()
        print('обратная дробь это')
        rev_frac = Fraction()
        rev_frac.set(self.numerator, self.denomerator)
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
            self.set(self.numerator // a, self.denomerator // a)
            self.print()
        else:
            print('Дробь')
            self.print()
            print('не может быть сокращена.')


frac1 = Fraction()
frac1.set(1, 5)
frac2 = Fraction()
frac2.set(14, 9)
frac3 = Fraction()
frac3.set(9, 7)
print(f'Правильных дробей:{Fraction.proper_fr_count}')
print(f'Неправильных дробей:{Fraction.improper_fr_count}')