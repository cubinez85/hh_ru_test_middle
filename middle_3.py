# def add_item(item, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(item)
#     return lst
# print(add_item(1))
# print(add_item(2))
# print(add_item())
#
#
# def run_rec(is_raining, temp):
#     if is_raining:
#         return 'Дождь'
#     elif temperature < 5:
#         return 'Холодно'
#     elif temperature >= 5 and temperature <= 15:
#         return 'На пробежку'
#     else:
#         return 'Жарко'
# raining = False
# temperature = 16
# print(run_rec(raining, temperature))

# def add_lst(val, lst=[]):
#     lst.append(val)
#     return lst
# lst1 = add_lst(1)
# lst2 = add_lst(2, [])
# lst3 = add_lst(3)
# print(lst1)
# print(lst2)
# print(lst3)


# def add_lst(val, lst=None):
#     if lst is None:
#         lst = []
#     lst.append(val)
#     return lst
#
#
# lst1 = add_lst(1)
# lst2 = add_lst(2, [])
# lst3 = add_lst(3)
# print(lst1)
# print(lst2)
# print(lst3)



# import time
# class Laptop:
#     def __init__(self):
#         self.power_on = False
#         self.battery_level = 10
#     def toggle_power(self):
#         if self.battery_level > 20:
#             self.power_on = not self.power_on
#             return f"Laptop power state: {'On' if self.power_on else 'Off' }"
#         else:
#             time.sleep(3)
#             self.power_on = False
#             return "Laptop is powered off due to low battery."
# my_laptop = Laptop()
# print(my_laptop.toggle_power())

# import csv
# from pprint import pprint
# data = []
# with open('./Orders_etl.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         data.append(row)
# pprint(data)

# import sys
#
# nums = [1, 2, 3, 4, 5]
# print(sys.getsizeof(nums))


# import tempfile
#
# with tempfile.NamedTemporaryFile(delete=False) as temp_file:
#     file_path = temp_file.name
#     print(f"Файл создан по адресу: {file_path}")

#
# import tempfile
# import os
#
# with tempfile.NamedTemporaryFile(delete=False) as temp_file:
#     temp_file.write(b"Some data")
#     file_path = temp_file.name
#
# try:
#     os.remove(file_path)
#     print(f"Файл '{file_path}' успешно удален.")
# except OSError as e:
#     print(f"Ошибка при удалении файла '{file_path}': {e}")



# import tempfile
#
# with tempfile.NamedTemporaryFile(delete=False) as temp_file:
#     temp_file.write(b"Hello, named temporary world!")
#     temp_file.seek(0)
#     print(temp_file.read())
#     file_path = temp_file.name  # Получаем имя файла
#
# # Файл все еще существует после выхода из блока 'with'
# print(f"Временный файл создан по адресу: {file_path}")
# # Его нужно удалить вручную, когда он больше не нужен.


# import tempfile
# fp = tempfile.NamedTemporaryFile(delete=False)
# fp.write(b'Hello world!')
# fp.seek(0)
# content = fp.read()
# print(content.decode('utf-8'))
# fp.close()


# import tempfile
#
# # Создаем временный файл
# fp = tempfile.TemporaryFile()
#
# # Записываем данные в файл
# fp.write(b'Hello world!')
#
# # Переходим в начало файла, чтобы прочитать его содержимое
# fp.seek(0)
#
# # Читаем содержимое файла и сохраняем в переменную
# content = fp.read()
#
# # Печатаем считанное содержимое
# print(content)
#
# # Закрываем временный файл
# fp.close()
#




# import re
# text = '123.45 678.9'
# pattern = r'\d+.\d+'
# result = re.search(pattern, text)
# print(result.group())




# def digital_root(n: int) -> int:
#     if not isinstance(n, int) or n < 1:
#         raise ValueError('Введите целое положительое число')
#     if n < 10:
#         return n
#     while n > 9:
#         n = sum(int(i) for i in str(n))
#     return n
#
#
# input_string = input()
# result = digital_root(int(input_string))
# print(result)

# def digital_root(n: int) -> int:
#     if n < 1:
#         raise ValueError('Invalid input')
#     if n < 10:
#         return n
#     while n > 9:
#         n = sum(int(i) for i in str(n))
#     return n
#
#
# try:
#     input_string = input()
#     result = digital_root(int(input_string))
#     print(result)
# except ValueError as e:
#     print(e)


# def digital_root(n: int) -> int:
#     if not isinstance(n, int) or n < 1:
#         raise ValueError('Введите положительное число')
#     if n < 10:
#         return n
#     else:
#         sum_of_digits = sum(int(i) for i in str(n))
#     return digital_root(sum_of_digits)
#
#
# def main():
#     while True:
#         data_input = input()
#         try:
#             result = digital_root(int(data_input))
#             print(result)
#             break
#         except ValueError as e:
#             print(e)
#         except TypeError as e:
#             print(e)
#
#
# if __name__ == '__main__':
#     main()




#
# def higher_than_average(input_string):
#     numbers = []
#     for i in input_string.split():
#         try:
#             num = int(i)
#             if num < 1:
#                 print('Введите целые положительные числа')
#                 return []
#             numbers.append(num)
#         except ValueError:
#             print('Введите целые положительные числа')
#             return []
#
#     if len(numbers) < 7 or len(numbers) > 31:
#         return None
#
#     high_days = []
#     for i in range(len(numbers)):
#         start_index = max(0, i - 3)
#         end_index = min(len(numbers), i + 4)
#         week_slice = numbers[start_index:end_index]
#         average_temp = sum(week_slice) / len(week_slice)
#         if numbers[i] > average_temp:
#             high_days.append(i)
#     if high_days:
#         return ' '.join(map(str, high_days))
#     else:
#         return 'Нет'
#
#
# temperature_series = input()
# result = higher_than_average(temperature_series)
# print(result)



# def higher_than_average(input_string):
#     try:
#         numbers = [int(i) for i in input_string.split()]
#         if not numbers:
#             return 'Введите значения'
#         elif not all(num > 0 for num in numbers):
#             return 'Введите значения больше 0'
#         elif not (7 <= len(numbers) <= 31):
#             return 'Длина списка от 7 до 31 включительно'
#     except ValueError:
#         return 'Введите целые числа'
#     high_days = []
#     for day_index, temperature in enumerate(numbers):
#         start_index = max(0, day_index - 3)
#         end_index = min(len(numbers), day_index + 4)
#         week_slice = numbers[start_index:end_index]
#         average_temp = sum(week_slice) / len(week_slice)
#         if temperature > average_temp:
#             high_days.append(day_index)
#     return ' '.join(map(str, high_days)) if high_days else 'Нет'
#
#
# temperature_series = input()
# result = higher_than_average(temperature_series)
# print(result)


# import math
#
# class Shape:
#     def __init__(self):
#         self.shape_type = None
#         self.side = 1
#         self.radius = 1
#
#     def initialize(self, shape_type, size=None):
#         self.shape_type = shape_type
#         if shape_type == 'квадрат':
#             self.side = size if size is not None else 1
#             self.radius = 0
#             if size is not None and size <= 0:
#                 raise ValueError(f'Размер стороны квадрата "{size}" должен быть больше 0')
#
#         elif shape_type == 'круг':
#             self.radius = size if size is not None else 1
#             self.side = 0
#             if size is not None and size <= 0:
#                 raise ValueError(f'Размер радиуса круга "{size}" должен быть больше 0')
#         else:
#             raise ValueError(f'Введите правильный тип фигуры {shape_type}')
#
#     def area(self):
#         if self.shape_type == 'квадрат':
#             return f'{self.side ** 2:.2f}'
#         elif self.shape_type == 'круг':
#             return f'{math.pi * self.radius ** 2:.2f}'
#         else:
#             raise ValueError(f'Неизвестный тип фигуры: {self.shape_type}')
#
#     def perimeter(self):
#         if self.shape_type == 'квадрат':
#             return f'{self.side * 4:.2f}'
#         elif self.shape_type == 'круг':
#             return f'{2 * math.pi * self.radius:.2f}'
#         else:
#             raise ValueError(f'Неизвестный тип фигуры: {self.shape_type}')
#
#
#
# input_data = input()
# data_parts = input_data.split()
# if not data_parts or len(data_parts) == 0:
#     print('Ошибка: Введите тип фигуры')
# else:
#     data_shape_type = data_parts[0]
#     data_size = None
#     if len(data_parts) > 1:
#         try:
#             data_size = float(data_parts[1])
#         except ValueError:
#             print('Ошибка: Размер должен быть числом')
#             data_size = None
#
#     shape = Shape()
#     try:
#         shape.initialize(data_shape_type, data_size)
#         print(f'{shape.area()} {shape.perimeter()}')
#     except ValueError as e:
#         print(e)
#     except TypeError as e:
#         print(e)


#
# import math
#
# class Shape:
#     def __init__(self):
#         self.shape_type = None
#         self.side = None
#         self.side2 = None
#         self.side3 = None
#         self.radius = None
#     def initialize(self, shape_type, size=None, size2=None, size3=None):
#         self.shape_type = shape_type
#         if shape_type == 'квадрат':
#             self.side = size if size is not None else 1
#             self.side2 = self.side
#             self.side3 = 0
#             self.radius = 0
#         elif shape_type == 'круг':
#             self.radius = size if size is not None else 1
#             self.side = 0
#             self.side2 = 0
#             self.side3 = 0
#         elif shape_type == 'прямоугольник':
#             self.side = size if size is not None else 1
#             self.side2 = size2 if size2 is not None else 2
#             self.side3 = 0
#             self.radius = 0
#         elif shape_type == 'треугольник':
#             self.side = size if size is not None else 4
#             self.side2 = size if size is not None else 5
#             self.side3 = size if size is not None else 6
#             self.radius = 0
#         else:
#             raise ValueError('Invalid type shape')
#     def area(self):
#         if self.shape_type == 'квадрат':
#             return round(self.side ** 2, 2)
#         elif self.shape_type == 'круг':
#             return round(math.pi * self.radius ** 2, 2)
#         elif self.shape_type == 'прямоугольник':
#             return round(self.side * self.side2, 2)
#         elif self.shape_type == 'треугольник':
#             s = (self.side + self.side2 + self.side3) / 2
#             sqrt = (s * (s - self.side) * (s - self.side2) * (s - self.side3)) ** 0.5
#             return round(sqrt, 2)
#         else:
#             return 0
#     def perimeter(self):
#         if self.shape_type == 'квадрат':
#             return round(self.side * 4, 2)
#         elif self.shape_type == 'круг':
#             return round(2 * math.pi * self.radius, 2)
#         elif self.shape_type == 'прямоугольник':
#             return round((self.side + self.side2) * 2, 2)
#         elif self.shape_type == 'треугольник':
#             return round(self.side + self.side2 + self.side3, 2)
#         else:
#             return 0
#
#
# input_data = input()
# data_parts = input_data.split()
# if not data_parts or len(data_parts) == 0:
#     print('Введите тип фигуры')
# else:
#     data_shape_type = data_parts[0]
#     data_size = None
#     data_size2 = None
#     data_size3 = None
#     if len(data_parts) > 1:
#         try:
#             data_size = float(data_parts[1])
#             if len(data_parts) > 2:
#                 data_size2 = float(data_parts[2])
#                 if len(data_parts) > 3:
#                         data_size3 = float(data_parts[3])
#             if data_shape_type == 'треугольник' and data_size3 is not None:
#                 sides = sorted([data_size, data_size2, data_size3])
#                 if sides[0] + sides[1] <= sides[2]:
#                     print('Не треугольник')
#                     exit()
#         except ValueError:
#             print('Размер должен быть числом')
#             exit()
#
#     shape = Shape()
#     try:
#         shape.initialize(data_shape_type, data_size2, data_size3)
#         print(f'Площадь: {shape.area()}, Периметр: {shape.perimeter()}')
#     except ValueError as e:
#         print(e)


#
# import math
#
# class Shape:
#     def __init__(self):
#         self.shape_type = None
#         self.height = None
#         self.radius = None
#
#     def initialize(self, shape_type, radius=None, height=None):
#         if shape_type.lower() != 'цилиндр':
#             raise ValueError('Неверный тип фигуры. Поддерживается только цилиндр.')
#         if radius is None or height is None:
#             raise ValueError('Для цилиндра необходимо указать радиус и высоту.')
#         self.shape_type = shape_type
#         self.radius = radius
#         self.height = height
#
#     def area(self):
#         if self.shape_type == 'цилиндр':
#             circle_area = math.pi * self.radius ** 2
#             rectangle_area = (2 * math.pi * self.radius) * self.height
#             return round(circle_area * 2 + rectangle_area, 2)
#         else:
#             return 0
#
#     def perimeter(self):
#         if self.shape_type == 'цилиндр':
#             circle_perimeter = 2 * math.pi * self.radius
#             rectangle_perimeter = circle_perimeter * 2 + self.height * 2
#             return round(circle_perimeter * 2 + rectangle_perimeter, 2)
#         else:
#             return 0
#
#
# input_data = input('Введите цилиндр радиус и высоту через пробел: ')
# data_parts = input_data.split()
# if not data_parts or len(data_parts) == 0:
#     print('Введите тип фигуры')
# else:
#     data_shape_type = data_parts[0]
#     try:
#         radius = float(data_parts[1]) if len(data_parts) > 1 else None
#         height = float(data_parts[2]) if len(data_parts) > 2 else None
#     except (ValueError, IndexError):
#         print('Размеры должны быть числами')
#         exit()
#
#     shape = Shape()
#     try:
#         shape.initialize(data_shape_type, radius, height)
#         print(f'Площадь: {shape.area()}, Периметр: {shape.perimeter()}')
#     except ValueError as e:
#         print(e)


#
# import math
#
# class Shape:
#     def __init__(self):
#         self.shape_type = None
#         self.height = None
#         self.radius = None
#
#     def initialize(self, shape_type, radius=None, height=None):
#         if shape_type.lower() != 'цилиндр':
#             raise ValueError('Неверный тип фигуры. Поддерживается только цилиндр.')
#         if radius is None or height is None:
#             raise ValueError('Для цилиндра необходимо указать радиус и высоту.')
#         self.shape_type = shape_type
#         self.radius = radius
#         self.height = height
#
#     def area(self):
#         if self.shape_type == 'цилиндр':
#             circle_area = math.pi * self.radius ** 2
#             rectangle_area = (2 * math.pi * self.radius) * self.height
#             return round(circle_area * 2 + rectangle_area, 2)
#         else:
#             return 0
#
#     def perimeter(self):
#         if self.shape_type == 'цилиндр':
#             circle_perimeter = 2 * math.pi * self.radius
#             rectangle_perimeter = circle_perimeter * 2 + self.height * 2
#             return round(circle_perimeter * 2 + rectangle_perimeter, 2)
#         else:
#             return 0
#
#
# def main():
#     input_data = input('Введите цилиндр, радиус и высоту: ')
#     data_parts = input_data.split()
#     if len(data_parts) < 1:
#         print('Введите тип фигуры')
#         return
#     data_shape_type = data_parts[0]
#     try:
#         radius = float(data_parts[1]) if len(data_parts) > 1 else None
#         height = float(data_parts[2]) if len(data_parts) > 2 else None
#     except ValueError:
#         print('Введите числовые значения для radius и height')
#         return
#
#
#     shape = Shape()
#     try:
#         shape.initialize(data_shape_type, radius, height)
#         print(f'Площадь: {shape.area()}, Периметр: {shape.perimeter()}')
#     except ValueError as e:
#         print(e)
#
#
# if __name__ == '__main__':
#     main()