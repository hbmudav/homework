def intro(obj):

    obj_type = type(obj).__name__ # Определение типа объекта

    attributes = [attribute for attribute in dir(obj) # Получение атрибутов объекта
                  if not callable(getattr(obj, attribute))]

    methods = [method for method in attributes if callable(getattr(obj, method))] # Получение методов объекта

    module = obj.__class__.__module__ # Определение модуля, к которому объект принадлежит

    info = {'type': obj_type, 'attributes': attributes, 'methods': methods, 'module': module}
    # Создание словаря с информацией об объекте

    return info

number_info = intro(42) # Интроспекция числа
print(number_info)

string_info = intro('Hello, World!') # Интроспекция строки
print(string_info)

list_info = intro(['1', 2, 3, 4.0]) # Интроспекция списка
print(list_info)