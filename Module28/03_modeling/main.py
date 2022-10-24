from typing import Any
from abc import ABC
import math


class Figure(ABC):
    """Абстрактный класс фигура"""

    def __init__(self, base: int, height: int) -> None:
        self.base = base
        self.height = height

    @property
    def base(self) -> int:
        return self.__base

    @base.setter
    def base(self, base: int) -> None:
        self.__base = base

    @property
    def height(self) -> int:
        return self.__height

    @height.setter
    def height(self, height: int):
        self.__height = height


class Square(Figure):

    def __init__(self, base: int) -> None:
        super().__init__(base=base, height=base)

    def square(self) -> int:
        return self.base * 2

    def perimetr(self) -> int:
        return self.base * 4


class Triangle(Figure):

    def square(self) -> float:
        return 1 / 2 * self.base * self.height

    def perimetr(self) -> float:
        return 2 * math.sqrt(self.base ** 2 - self.height ** 2) + 2 * self.base


class FullSquareMixin:
    figure_list = []
    full_square = 0

    def calculate(self) -> Any:
        for item in list(self.figure_list):
            self.full_square += item.square()
        return self.full_square


class Cube(FullSquareMixin):
    def __init__(self, base: int):
        self.figure_list = [Square(base) for _ in range(6)]


class Pyramid(FullSquareMixin):
    def __init__(self, base: int, height: int):
        self.figure_list = [Triangle(base=base, height=height) for _ in range(4)]
        self.figure_list.append(Square(base=base))


cube_1 = Cube(4)
print(cube_1.calculate())
pyramid_1 = Pyramid(4, 6)
print(pyramid_1.calculate())
