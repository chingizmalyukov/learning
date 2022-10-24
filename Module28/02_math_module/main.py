import math


class MyMath:
    """Класс с формулами из математики"""
    import math

    @classmethod
    def circle_len(cls, radius: int) -> float:
        return 2 * math.pi * radius

    @classmethod
    def circle_sq(cls, radius: int) -> float:
        return math.pi * radius ** 2

    @classmethod
    def circle_vol(cls, radius: int, h: int) -> float:
        return math.pi * radius ** 2 * h

    @classmethod
    def sphere(cls, radius: int) -> float:
        return math.pi * 4 * radius ** 2


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
