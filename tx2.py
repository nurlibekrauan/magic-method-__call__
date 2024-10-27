class LimitCalls:
    def __init__(self, max_calls):
        self.max_calls = max_calls

    def __call__(self, cls):
        # Обрабатываем каждый метод класса
        for attr_name in dir(cls):
            attr = getattr(cls, attr_name)
            if callable(attr) and not attr_name.startswith("__"):
                # Оборачиваем метод в декоратор
                decorated_method = self.dec_calls(self.max_calls)(attr)
                setattr(cls, attr_name, decorated_method)
        return cls

    def dec_calls(self, max_calls):
        def dec_func(func):
            def wrapper(*args, **kwargs):
                if not hasattr(wrapper, "calls"):
                    wrapper.calls = 0
                if wrapper.calls > max_calls:
                    raise Exception("Too many calls")
                wrapper.calls += 1
                return func(*args, **kwargs)

            return wrapper

        return dec_func


@LimitCalls(max_calls=3)
class Printer:
    def print_message(self, message):
        print(message)


p = Printer()
p.print_message("Hello")
p.print_message("World")
p.print_message("!")
try:
    p.print_message("This will raise an exception")  # Тут будет исключение
except:
    print("ошибка")
