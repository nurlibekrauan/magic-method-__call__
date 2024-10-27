class CacheDecorator:
    def __call__(self, cls):
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if callable(attr) and not attr_name.startswith("__"):
                setattr(cls, attr_name, self.cache_decorator(attr))
        return cls

    def cache_decorator(self, func):
        # Создаем кеш в методе декоратора, чтобы он не перезаписывался
        cache = {}

        def wrapper(self, *args, **kwargs):
            if args not in cache:
                cache[args] = func(self, *args, **kwargs)
            return cache[args]

        return wrapper


@CacheDecorator()
class Calculator:
    def factorial(self, n):
        if n == 0:
            return 1
        return n * self.factorial(n - 1)


calc = Calculator()
print(calc.factorial(5))  # Вычисляется заново
print(calc.factorial(5))  # Берется из кеша
print(calc.factorial(4))  # Вычисляется заново
