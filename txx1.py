class Logger:
    def __call__(self, cls):
        original_init = cls.__init__

        def new_init(self, *args, **kwargs):
            # логируем иницализаццю класса
            with open(f"log_{cls.__name__}.log", "a+",encoding='utf-8') as f:
                f.write(
                    f"Класс {cls.__name__} инициализирован с аргументами {args}, {kwargs}\n"
                )
            # Вызываем оригинальный метод __init__
            original_init(self, *args, **kwargs)

        cls.__init__ = new_init
        # Оборачиваем каждый метод класса в декоратор
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if callable(attr) and not attr_name.startswith("__"):
                decorated_method = self.log_method(attr)
                setattr(cls, attr_name, decorated_method)
        return cls

    def log_method(self, func):
        def wrapper(*args, **kwargs):
            # Логируем вызов метода
            with open(f"log_{type(args[0]).__name__}.log", "a+",encoding='utf-8') as f:

            
                f.write(
                    f"Метод {func.__name__} вызван с аргументами {args}, {kwargs}\n"
                )
            return func(*args, **kwargs)

        return wrapper


@Logger()
class MyClass:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def multiply(self):
        return self.x * self.y
    


# Создаем объект и вызываем методы
obj = MyClass(2, 3)  # Логирование инициализации
print(obj.add())  # Логирование вызова метода add
print(obj.multiply())  # Логирование вызова метода multiply
