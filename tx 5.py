import time

class ExecutionTimer:
    def decorator(self, func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Execution time for {func.__name__}: {end_time - start_time} seconds")
            return result
        return wrapper

    def __call__(self, cls):
        for i in dir(cls):
            if callable(getattr(cls, i)) and not i.startswith('__'):  # Исключаем магические методы
                original_func = getattr(cls, i)
                decorated_func = self.decorator(original_func)
                setattr(cls, i, decorated_func)
        return cls


@ExecutionTimer()
class DataProcessor:
    def process(self, data):
        # Симуляция обработки данных
        time.sleep(2)
        return data


dp = DataProcessor()
dp.process("test")
