'''1.	Определите класс “Прямая” со свойствами:  координаты двух точек (x1, y1) и (x2, y2)
методами: вывод уравнения прямой и  определение точек пересечения с осями координат.'''


class Line():
    line_count = 0
    par_axis_count = 0
    through_the_origin = 0

    def set(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        Line.line_count += 1
        if self.x1 != self.x2:
            self.dx = round(self.x2 - self.x1)
        if self.y1 != self.y2:
            self.dy = round(self.y2 - self.y1)
        if self.x2 == self.x1 or self.y1 == self.y2:
            Line.par_axis_count += 1
        elif (self.x1 / (self.x2 - self.x1)) == (self.y1 / (self.y2 - self.y1)):
            Line.through_the_origin += 1

    def equation_line(self):
        if self.x2 == self.x1:
            print(f"Уравнение прямой x={self.x1}, прямая параллельна оси OY")
        elif self.y1 == self.y2:
            print(f"Уравнение прямой y={self.y1}, прямая параллельна оси OX")
        else:
            k = round(self.dy / self.dx, 2)
            b = round((-1) * (self.dy / self.dx) * self.x1 + self.y1, 2)
            print(f"Точки: М1({self.x1};{self.y1}) и М2({self.x2};{self.y2})")
            print(f"Уравнение прямой, проходящей через эти точки: y={k}*x{b:+}")


    def intersection_points(self):
        if self.x1 == self.x2:
            print(f"Точка пересечения с осью OY: не пересекается.")
            print(f"Точка пересечения с осью OX:({self.x1};0)")
        elif self.y1 == self.y2:
            print(f"Точка пересечения с осью OY:(0;{self.y1}")
            print(f"Точка пересечения с осью OX: не пересекается.")
        else:
            k = round(self.dy / self.dx, 2)
            b = round((-1) * (self.dy / self.dx) * self.x1 + self.y1, 2)
            print(f"Точка пересечения с осью OY:(0;{b})")
            print(f"Точка пересечения с осью OX:({(-1) * (b / k)};0)")


line = Line()
line.set(2, 1, -2, -1)
line1 =Line()
line1.set(5, 3, 5, 3)
line2 =Line()
line2.set(1, 3, 5, 2)
line3 = Line()
line3.set(4, 1, -4, -1)
print(f'Количество прямых: {Line.line_count}')
print(f'Прямые параллельные осям: {Line.par_axis_count}')
print(f'Прямые проходят через начало координат: {Line.through_the_origin}')
