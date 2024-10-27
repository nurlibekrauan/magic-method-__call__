class DataInitializer:
    def __init__(self):
        self.default_data = {"a": 1, "b": 2, "c": 3}  # Данные для инициализации

    def get_data(self):
        return self.default_data


def initialize_with_data(cls):
    """Декоратор класса, который внедряет данные из DataInitializer."""
    
    original_init = cls.__init__  # Сохраняем оригинальный метод __init__

    def new_init(self, *args, **kwargs):
        # Создаем экземпляр класса DataInitializer и получаем данные
        initializer = DataInitializer()
        self.initialized_data = initializer.get_data()  # Инициализируем данные

        # Вызываем оригинальный __init__, чтобы не нарушить логику
        original_init(self, *args, **kwargs)

    cls.__init__ = new_init  # Заменяем оригинальный метод __init__
    
    return cls


@initialize_with_data
class MyClass:
    def __init__(self, name):
        self.name = name  # Инициализация передаваемых данных

    def print_data(self):
        print(f"Name: {self.name}, Initialized Data: {self.initialized_data}")


# Использование декорируемого класса
obj = MyClass("TestObject")
obj.print_data()
