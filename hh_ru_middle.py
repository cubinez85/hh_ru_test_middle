# def max_sequence_sum(numbers: str, sequence_length: str) -> str:
#     try:
#         lst_numbers = [int(i) for i in numbers.split()]
#         length = int(sequence_length)
#     except ValueError:
#         return 'Введите целые числа'
#     if length > len(lst_numbers):
#         return 'Invalid input'
#     if length < 1:
#         return 'Введите положительное число'
#     all_positive = all(num > 0 for num in lst_numbers)
#     all_negative = all(num < 0 for num in lst_numbers)
#     is_increasing = all(lst_numbers[i] < lst_numbers[i+1] for i in range(len(lst_numbers) - 1))
#     is_decreasing = all(lst_numbers[i] > lst_numbers[i+1] for i in range(len(lst_numbers) - 1))
#     if not ((all_positive and is_increasing) or (all_negative and is_decreasing)):
#         return 'Последовательность должна быть строго возрастающей положительной или строго убывающей отрицательной'
#     if is_increasing and all_positive:
#         return str(sum(lst_numbers[-length:]))
#     else:
#         return str(sum(lst_numbers[:length]))
#
#
# numbers_list = input()
# sequence_length = input()
# result = max_sequence_sum(numbers_list, sequence_length)
# print(result)




# def process_employee_data(input_string: str) -> str:
#     ages = []
#     employee_records = input_string.split(';')
#     if not (2 <= len(employee_records) <= 100):
#         return 'Invalid input'
#     for employee_record in employee_records:
#         record_parts = employee_record.split(',')
#         if len(record_parts) < 2:
#             continue
#         try:
#             age = int(record_parts[1])
#             ages.append(age)
#         except ValueError:
#             return 'Введите целые числа'
#     if not ages:
#         return 'Invalid input'
#     min_age = min(ages)
#     max_age = max(ages)
#     sort_lst = sorted(ages)
#     mid_index = len(sort_lst) // 2
#     if len(sort_lst) % 2 == 0:
#         median = (sort_lst[mid_index - 1] + sort_lst[mid_index]) / 2
#     else:
#         median = sort_lst[mid_index]
#     return f'{min_age} {round(median)} {max_age}'
#
#
# input_data = input()
# output_data = process_employee_data(input_data)
# print(output_data)



# def analyze_sales(input_strings):
#     if not input_strings:
#         return ['No data']
#     products = input_strings[:-1]
#     try:
#         limit = int(input_strings[-1])
#     except ValueError:
#         return [f'Invalid input: Enter integers in "{input_strings[-1]}"']
#     if not (0 < len(products) <= 100):
#         return ['Invalid input: Number of products out of range']
#     results = []
#     for item in products:
#         parts = item.split(',')
#         if not parts or not parts[0]:
#             return ["Invalid input: Product name is missing"]
#         name = parts[0]
#         prices = []
#         if len(parts) > 1:
#             try:
#                 prices = [int(i) for i in parts[1:]]
#             except ValueError:
#                 return [f'Invalid input: Enter integers in "{', '.join(parts[1:])}"']
#         if prices:
#             average_price = sum(prices) / len(prices)
#             if average_price > limit:
#                 results.append((name, average_price))
#     results.sort(key=lambda x: (-x[1], x[0]))
#     total = [f'{name},{average_price:.1f}' for name, average_price in results]
#     if results:
#         return total
#     else:
#         return ['Нет данных']
#
#
# lines = []
# while True:
#     try:
#         line = input()
#         if line == '':
#             break
#     except EOFError:
#         break
#     lines.append(line)
# for product in analyze_sales(lines):
#     print(product)



#
# def solve(input_string: str) -> list:
#     if not input_string.split():
#         return ['Ошибка: входная строка не может быть пустой']
#     # Преобразуем строку в список целых чисел.
#     try:
#         lst = list(map(int, input_string.split()))
#     except ValueError:
#         return ["Ошибка: неверный формат входных данных."]
#
#     # Проверяем, что длина списка не больше 100.
#     if len(lst) > 100:
#         return ["Ошибка: длина списка не больше 100."]
#
#     increasing_sequences = []  # Список для хранения найденных последовательностей.
#     current_sequence = []  # Список для текущей возрастающей последовательности.
#
#     # Проходим по элементам списка.
#     for i in range(len(lst)):
#         # Если текущая последовательность пустая, добавляем элемент.
#         if not current_sequence:
#             current_sequence.append(lst[i])
#         else:
#             # Проверяем, увеличивается ли текущее значение по сравнению с предыдущим.
#             if lst[i] > current_sequence[-1]:
#                 current_sequence.append(lst[i])  # Добавляем элемент в текущую последовательность.
#             else:
#                 # Если последовательность прерывается, сохраняем текущую и начинаем новую.
#                 if len(current_sequence) > 1:  # Сохраняем только если длина больше 1.
#                     increasing_sequences.append(current_sequence)
#                 current_sequence = [lst[i]]  # Начинаем новую последовательность.
#
#     # Проверяем последнюю последовательность
#     if len(current_sequence) > 1:
#         increasing_sequences.append(current_sequence)
#
#     # Вывод результата
#     if increasing_sequences:
#         return [' '.join(map(str, sequence)) for sequence in increasing_sequences]
#     else:
#         return ['Не обнаружено']
#
#
# input_string = input()
# results = solve(input_string)
# for result in results:
#     print(result)




# class PointDistanceCalculator:
#     def __init__(self, input_string):
#         lst = input_string.split()
#         if len(lst) != 4:
#             raise ValueError('Ошибка: Введите 4 числа')
#         try:
#             self.x1, self.y1, self.x2, self.y2 = map(int, lst)
#         except ValueError:
#             raise ValueError('Ошибка: Введите целые числа')
#     def calculate_distance(self):
#         import math
#         distance = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
#         return round(distance, 2)
#
#
# input_string = input()
# calculator = PointDistanceCalculator(input_string)
# print(calculator.calculate_distance())


# def digital_root(n: int) -> int:
#     if not isinstance(n, int) or n < 1:
#         raise ValueError('Invalid input')
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


# def solve(input_string: str) -> str:
#     try:
#         lst = [int(i) for i in input_string.split()]
#     except ValueError:
#         return 'Ошибка: Введите целые числа'
#     if len(lst) > 100:
#         return 'Ошибка: Длина списка не больше 100 элементов'
#
#     data_max = []
#     for i in range(len(lst)):
#         if not data_max:
#             data_max.append(lst[i])
#         else:
#             if lst[i] > data_max[-1]:
#                 data_max.append(lst[i])
#             else:
#                 data_max.append(data_max[-1])
#     return ' '.join(map(str, data_max))
#
#
# input_string = input()
# result = solve(input_string)
# print(result)




# special_symbols = "!@#$%^&*()-+"
#
#
# class CheckPasswords:
#     def __init__(self, passwords):
#         self.passwords = passwords.split()
#
#
#     def is_safe_password(self, password):
#         if len(password) < 8:
#             return False
#         if not any(char in special_symbols for char in password):
#             return False
#         if not any(char.isdigit() for char in password):
#             return False
#         if not any(char.isupper() for char in password):
#             return False
#         if not any(char.islower() for char in password):
#             return False
#         return True
#
#
#     def solve(self):
#         if not (1 <= len(self.passwords) <= 100):
#             return 'Invalid input: Length self.passwords must be not more 100'
#         safe_passwords = []
#         for password in self.passwords:
#             result = self.is_safe_password(password)
#             if result:
#                 safe_passwords.append(password)
#         if not safe_passwords:
#             return 'Не найдено'
#         return ' '.join(safe_passwords)
#
#
# input_string = input()
# check = CheckPasswords(input_string)
# print(check.solve())




# def count_vowels_and_consonants(text: str):
#     if not (1 <= len(text) <= 100):
#         return 'Invalid input: Length text must be from 1 to 100'
#     count_vowels = 0
#     count_consonants = 0
#     from string import punctuation
#     vowels_chars = set('ауоиэыяюеё')
#     clean_text = ''.join(char for char in text.lower() if char not in punctuation)
#     for letter in clean_text:
#         if letter in vowels_chars:
#             count_vowels += 1
#         elif letter.isalpha():
#             count_consonants += 1
#     return count_vowels, count_consonants
#
#
# input_string = input()
# vowels, consonants = count_vowels_and_consonants(input_string)
# print(vowels, consonants)


# def analyze_sales(input_strings):
#     products_dict = {}
#     results = []
#     total_products = 0
#     for part in input_strings:
#         parts_products = part.split(',')
#         if len(parts_products) != 3:
#             return 'Invalid input: Length parts must be equal to 3'
#         name, category, price = parts_products
#         try:
#             price = float(price)
#         except ValueError:
#             return f'Invalid input: "{price}" must be number'
#         total_products += 1
#         if total_products > 100:
#             return 'Invalid input: Total number of products exceeds 100'
#         if category not in products_dict:
#             products_dict[category] = []
#         products_dict[category].append((name, price))
#     for category, items in products_dict.items():
#         items.sort(key=lambda x: (x[1], x[0]))
#         results.append(f'{category}:')
#         for item in items:
#             results.append(f'{item[0]},{item[1]}')
#     return results
#
#
# lines = []
# while True:
#     try:
#         line = input()
#         if line == '':
#             break
#     except EOFError:
#         break
#     lines.append(line)
# for product in analyze_sales(lines):
#     print(product)



# def get_cold_days(temperatures: str) -> str:
#     if not temperatures:
#         return 'Invalid input: Empty data'
#     try:
#         temp_lst = [int(temp) for temp in temperatures.split()]
#     except ValueError:
#         return 'Invalid input: Enter integers'
#     if len(temp_lst) > 100:
#         return 'Invalid input: Length must be <= 100'
#     cold_days_indexes = []
#     for i in range(1, len(temp_lst)):
#         if temp_lst[i] < temp_lst[i - 1] - 2:
#             cold_days_indexes.append(i)
#     return ' '.join(map(str, cold_days_indexes)) if cold_days_indexes else 'Нет'
#
#
# temperatures = input()
# cold_days = get_cold_days(temperatures)
# print(cold_days)




#
# import re
#
# class TextProcessor:
#     def __init__(self, text):
#         self.text = text
#
#     def extract_emails(self):
#         if not isinstance(self.text, str):
#             return 'Invalid input: Text must be a string'
#         if len(self.text) > 1000:
#             return 'Invalid input: Length text must be <= 1000'
#         email_regex = r'\b[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.(?:ru|com|net|org)\b'
#         emails = re.findall(email_regex, self.text)
#         unique_emails = set(emails)
#         if unique_emails:
#             return '\n'.join(sorted(unique_emails))
#         else:
#             return 'Не найдено'
#
#
# input_string = input()
# textprocessor = TextProcessor(input_string)
# print(textprocessor.extract_emails())


# def select_candidates(candidate_strings):
#     if not candidate_strings:
#         return ['Error: Empty data']
#     if not (2 <= len(candidate_strings) <= 100):
#         return ['Error: Length strings of candidates is out of range (2,100)']
#     surnames = []
#     for block in candidate_strings:
#         surname = block.split(',')[0]
#         surnames.append(surname)
#         if len(surnames) != len(set(surnames)):
#             return ['Error: All surnames must be unique']
#     passed_candidates = []
#     for block in candidate_strings:
#         data_string = block.split(',')
#         surname_candidate = data_string[0]
#         if len(data_string) > 1:
#             try:
#                 scores = [int(score) for score in data_string[1:]]
#                 average_score = sum(scores) / len(scores)
#                 if average_score >= 5:
#                     passed_candidates.append((surname_candidate, average_score))
#             except ValueError:
#                 return ['Error: Enter integers']
#     passed_candidates.sort(key=lambda x: (-x[1], x[0]))
#     total = [f'{surname_candidate},{average_score:.1f}' for surname_candidate, average_score in passed_candidates]
#     if passed_candidates:
#         return total
#     else:
#         return ['Никто']
#
#
# lines = []
# while True:
#     try:
#         line = input()
#         if line == '':
#             break
#     except EOFError:
#         break
#     lines.append(line)
# print(lines)
# for candidate in select_candidates(lines):
#     print(candidate)
