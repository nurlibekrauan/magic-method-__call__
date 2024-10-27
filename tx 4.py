class CacheResults:
    def __call__(self, cls):
        self.cache = {}  # Кэш для хранения результата
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if callable(attr) and not attr_name.startswith("__"):
                setattr(cls, attr_name, self.cache_decorator(attr))
        return cls

    def cache_decorator(self, func):
        def wrapper(instance, arg):  # В этом случае передаем только один аргумент
            if arg not in self.cache:  # Используем число как ключ
                self.cache[arg] = func(instance, arg)
            return self.cache[arg]

        return wrapper


@CacheResults()
class FactorialCalculator:
    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)


calc = FactorialCalculator()
print(calc.factorial(5))  # Вычисляется заново
print(calc.factorial(5))  
