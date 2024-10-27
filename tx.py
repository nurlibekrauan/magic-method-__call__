import os
os.chdir(os.path.dirname(__file__))
class Logger:
    def __init__(self, cls):
        self.cls = cls
        self.file_name = "log_" + cls.__class__.__name__ + ".log"
        self.file = open(self.file_name,'a+',encoding='utf-8')

    def __call__(self, *args, **kwargs):
        obj = self.cls(*args, **kwargs)  # obj это объект который мы вызываем

        for attr_name in dir(obj):
            attr = getattr(obj, attr_name)  # attr это атроибут нашего объекта
            if callable(attr) and not attr_name.startswith("__"):
                setattr(obj, attr_name, self.log_method(attr))

        return obj

    def log_method(self, method):
        def wrapper(*args, **kwargs):
            method_name = method.__name__
            self.file.write(f'ММетода [{method_name}] вызван с аргументами {args} {kwargs}\n')
            print(f"Метода [{method_name}] вызван с аргументами {args} {kwargs}")
            result = method(*args, **kwargs)
            return result

        return wrapper


@Logger
class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b


calc = Calculator()
calc.add(2, 3)
calc.multiply(4, 5)
