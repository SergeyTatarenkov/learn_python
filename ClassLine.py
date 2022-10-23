'''1.	Определите класс “Прямая” со свойствами:  координаты двух точек (x1, y1) и (x2, y2)
методами: вывод уравнения прямой и  определение точек пересечения с осями координат.'''


class Line():
    x1 = 5.0
    y1 = 2.0
    x2 = 6.0
    y2 = 4.0

    def equation_line(self):
        if self.x2 == self.x1:
            print(f"Уравнение прямой x={self.x1}, прямая параллельна оси OY")
        elif self.y1 == self.y2:
            print(f"Уравнение прямой y={self.y1}, прямая параллельна оси OX")
        else:
            dx = round(self.x2 - self.x1, 2)
            dy = round(self.y2 - self.y1, 2)
            k = round(dy / dx, 2)
            b = round((-1) * (dy / dx) * self.x1 + self.y1, 2)
            print(f"Точки: М1({self.x1};{self.y1}) и М({self.x2};{self.y2})")
            print(f"Уравнение прямой, проходящей через эти точки: y={k}*x{b:+}")

    def intersection_points(self):
        if self.x1 == self.x2:
            print(f"Точка пересечения с осью OY: не пересекается.")
            print(f"Точка пересечения с осью OX:({self.x1};0)")
        elif self.y1 == self.y2:
            print(f"Точка пересечения с осью OY:(0;{self.x1}")
            print(f"Точка пересечения с осью OX: не пересекается.")
        else:
            dx = round(self.x2 - self.x1, 2)
            dy = round(self.y2 - self.y1, 2)
            k = round(dy / dx, 2)
            b = round((-1) * (dy / dx) * self.x1 + self.y1, 2)
            print(f"Точка пересечения с осью OY:(0;{b})")
            print(f"Точка пересечения с осью OX:({(-1) * (b / k)};0)")


line = Line()
line.equation_line()
line.intersection_points()