# функтор
class StripChars:
    def __init__(self, chars) -> None:
        self.__counter = 0
        self.__chars = chars

    def __call__(self, *args, **kwargs):
        if not isinstance(args[0], str):
            raise TypeError("Input must be a string")
        return args[0].strip(self.__chars)


s1 = StripChars(" ")
res = s1(" Hello world! ")
s2 = StripChars("! ")
res2 = s2(" Hello world! ")
print(res, res2, sep="\n")


# классы декораторы
class Devirate:
    def __init__(self, func) -> None:
        self.__fn = func

    def __call__(self, x, dx=0.00001):
        return (self.__fn(x + dx) - self.__fn(x)) / dx


from math import sin, pi


@Devirate
def df_sin(x):
    return sin(x)


print(df_sin(pi / 3))
