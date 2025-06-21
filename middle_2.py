# def calculate_discount(item_count, total_order_amount):
#     discount_for_items = 10
#     discount_for_sum = 5
#     total_discount = discount_for_items + discount_for_sum
#     if not isinstance(item_count, int) or not isinstance(total_order_amount, (int, float)):
#         return 'Недопустимые значения для количества товаров или суммы заказа'
#     if item_count > 10 and total_order_amount < 100:
#         return discount_for_items
#     elif item_count > 10 and total_order_amount > 100:
#         return total_discount
#     elif item_count < 10 and total_order_amount > 100:
#         return discount_for_sum
#     else:
#         return 'Нет скидок'
#
#
# print(calculate_discount(34, 56))
# print(calculate_discount(23, 123))
# print(calculate_discount(4, 234))
# print(calculate_discount(3,45))
# print(calculate_discount(2.3, 'w'))



# for device_id in range(1, 4):
#     if device_id == 2:
#         continue
#     print('Проверка устройства', device_id)
# print('Проверка завершена')




# def frequent(elements, count):
#     element_count = {}
#     for element in elements:
#         if element in element_count:
#             element_count[element] += 1
#         else:
#             element_count[element] = 1
#     return [element for element in element_count if element_count[element] > count]
#
# elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana', 'apple']
# count = 2
# result = frequent(elements, count)
# print(result)


# from collections import Counter
#
# def frequent(elements, min_count):
#     element_counts = Counter(elements)
#     print(element_counts)
#     print(element_counts.items())
#     print(element_counts.keys())
#     print(element_counts.values())
#     return [element for element, count in element_counts.items() if count > min_count]
#
#
# elements = ['apple', 'banana', 'apple', 'orange', 'banana', 'banana', 'apple']
# min_count = 2
# result = frequent(elements, min_count)
# print(result)


# from collections import Counter

# def frequent(elements, count_threshold):
#     if not elements:
#         return []
#     element_counts = Counter(elements)
#     frequent_elements = [element for element, freq in element_counts.items() if freq > count_threshold]
#     return frequent_elements
#
#
# data_elements_str = input()
# data_elements = data_elements_str.split()
# data_count_str = input()
# try:
#     data_count = int(data_count_str)
# except ValueError:
#     print('Ошибка: введите целое число')
#     exit()
# result = frequent(data_elements, data_count)
# if result:
#     str_res = ' '.join(result)
#     print(f'Чаще "{data_count}" раз встречаются: "{str_res}"')
# else:
#     print('Нет данных')


# element_counts = {}
# element_counts['apple'] = element_counts.get('apple', 0) + 1
# print(element_counts)


# def frequent(elements, count):
#     if not elements:
#         return 'Error: Empty data'
#     lst_elements = elements.split()
#     try:
#         count_threshold = int(count)
#     except ValueError:
#         return 'Ошибка: количество элементов должно быть целым числом.'
#
#     element_counts = {}
#     for element in lst_elements:
#         element_counts[element] = element_counts.get(element, 0) + 1
#
#     frequent_elements = {element: freq for element, freq in element_counts.items() if freq > count_threshold}
#
#     if not frequent_elements:
#         return f'Нет элементов, которые встречаются чаще, чем {count_threshold} раз.'
#
#     str_res = ' '.join(frequent_elements.keys())
#
#     return f'Элементы, встречающиеся чаще {count} раз: {str_res}'
#
#
# def main():
#     data_elements = input("Введите элементы через пробел: ")
#     data_count = input('Введите количество элементов: ')
#     result = frequent(data_elements, data_count)
#     print(result)
#
#
# if __name__ == '__main__':
#     main()


# lst = ['banana', 'apple', 'banana']
# dict = {}
# count = 1
# for elem in lst:
#     if elem in dict:
#         dict[elem] += 1
#     else:
#         dict[elem] = 1
# res = {elem: freq for elem, freq in dict.items() if freq > 1}
# str_res = ' '.join(elem for elem in res)
# print(f'элемент "{str_res}" встречается чаще {count} раз')



# lst = ['banana', 'apple', 'banana']
# dict = {}
# count = 1
# for elem in lst:
#     if elem in dict:
#         dict[elem] += 1
#     else:
#         dict[elem] = 1
# frequent_words = {elem: freq for elem, freq in dict.items() if freq > count}
# if frequent_words:
#     str_res = ' '.join(frequent_words.keys())
#     item_count = ' '.join(map(str, frequent_words.values()))
#     print(f'элемент "{str_res}" встречается чаще "{count}" раз, "{item_count}" раза')
# else:
#     print('Нет данных')


# age = 18
# print('child' if age < 18 else 'old')



# def process_employee_data(input_string: str) -> str:
#     if not input_string:
#         return 'Error: Empty data'
#     lst_ages = []
#     blocks_lst = input_string.split(';')
#     if not (2 <= len(blocks_lst) <= 100):
#         return 'Error: Length of list employees is out of range(2,100)'
#     for block in blocks_lst:
#         parts_of_lst = block.split(',')
#         if len(parts_of_lst) != 3:
#             return 'Error: Invalid employee data format'
#         name, age, office = parts_of_lst
#         try:
#             age = int(age)
#         except ValueError:
#             return 'Error: Enter integer'
#         lst_ages.append(age)
#     lst_ages.sort()
#     min_age = lst_ages[0]
#     max_age = lst_ages[-1]
#     mid_index = len(lst_ages) // 2
#     if len(lst_ages) % 2 == 0:
#         median = (lst_ages[mid_index - 1] + lst_ages[mid_index]) / 2
#     else:
#         median = lst_ages[mid_index]
#     return f'{min_age} {median:.0f} {max_age}'
#
#
# input_data = input()
# output_data = process_employee_data(input_data)
# print(output_data)



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




# def process_employee_data(input_string: list[str]) -> str:
#     if not (2 <= len(input_string) <= 100):
#         return 'Error: Length of list employees is out of range(2,100)'
#     ages_lst = []
#     for part in input_string:
#         parts = part.split(',')
#         if len(parts) != 3:
#             return 'Error: Invalid employee data format'
#         name, age, office = parts
#         try:
#             age = int(age)
#             ages_lst.append(age)
#         except ValueError:
#             return 'Error: Enter integer'
#     if ages_lst:
#         ages_lst.sort()
#         min_age = ages_lst[0]
#         max_age = ages_lst[-1]
#         mid_index = len(ages_lst) // 2
#         if len(ages_lst) % 2 == 0:
#             median = (ages_lst[mid_index-1] + ages_lst[mid_index]) / 2
#         else:
#             median = ages_lst[mid_index]
#         return f'{min_age} {median:.0f} {max_age}'
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
# if lines:
#     output_data = process_employee_data(lines)
#     if output_data.startswith('Error'):
#         print(output_data)
#     else:
#         print(output_data)




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





# import unittest
#
# def analyze_sales(input_strings):
#     if not input_strings:
#         return ["No data"]
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
#         if len(parts) > 1:
#             try:
#                 prices = [int(i) for i in parts[1:]]
#             except ValueError:
#                 return [f'Invalid input: Enter integers in "{', '.join(parts[1:])}"']
#         if prices:
#             average_price = sum(prices) / len(prices)
#             if average_price > limit:  # Keep only averages > limit
#                 results.append((name, average_price))
#     results.sort(key=lambda x: (-x[1], x[0]))
#     total = [f'{name},{average_price:.1f}' for name, average_price in results]
#     if results: #after filtering by average_price > limit
#         return total
#     else:
#         return ["No data"]  # Only 'No data' if *nothing* passes the limit
#
# class TestAnalyzeSales(unittest.TestCase):
#
#     def test_invalid_price_format(self):
#         input_data = ["Product,abc,123", "50"]
#         expected_output = ['Invalid input: Enter integers in "abc, 123"']
#         self.assertEqual(analyze_sales(input_data), expected_output)
#
#     def test_empty_input(self):
#         input_data = []
#         expected_output = ["No data"]
#         self.assertEqual(analyze_sales(input_data), expected_output)
#
#     def test_missing_product_name(self):
#         input_data = [",10,20", "50"]
#         expected_output = ["Invalid input: Product name is missing"]
#         self.assertEqual(analyze_sales(input_data), expected_output)
#
#
#     def test_valid_input(self):
#         input_data = ["Product2,40,50", "15"]
#         expected_output = ['Product2,45.0']
#         self.assertEqual(analyze_sales(input_data), expected_output)
#
#     def test_no_data(self):
#       input_data = ["Product1,10,20", "Product2,30,40", "60"]
#       expected_output = ["No data"]
#       self.assertEqual(analyze_sales(input_data), expected_output)
#
#     def test_invalid_limit(self):
#         input_data = ["Product1,10,20,30", "abc"]
#         expected_output = ['Invalid input: Enter integers in "abc"']
#         self.assertEqual(analyze_sales(input_data), expected_output)
#
# if __name__ == '__main__':
#     unittest.main()
#



# def analyze_sales(input_strings):
#     limit = int(input_strings[-1])
#     products = input_strings[:-1]
#     if len(products) > 100:
#         print("Invalid input")
#         return
#     results = []
#     for item in products:
#         parts = item.split(',')
#         if len(parts) < 2:
#             print(f'Неверный формат ввода для продукта: {item}')
#             continue
#         name = parts[0]
#         try:
#             prices = list(map(int, parts[1:]) if len(parts) > 1 else [])
#         except ValueError as e:
#             print(f'Ошибка при вводе цен для {name}: {e}')
#             continue
#         if prices:
#             average_price = sum(prices) / len(prices)
#             if average_price > limit:
#                 results.append(f'{name},{average_price:.1f}')
#     if results:
#         return sorted(results, key=lambda x: (-float(x.split(',')[1]), x.split(',')[0]))
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





# def sort_key(items):
#     parts = items.split(',')
#     return -float(parts[1]), parts[0]
#
# def analyze_sales(input_strings):
#     limit = int(input_strings[-1])
#     products = input_strings[:-1]
#     if len(products) > 100:
#         print("Invalid input")
#         return
#     results = []
#     for item in products:
#         parts = item.split(',')
#         if len(parts) < 2:
#             print(f'Неверный формат ввода для продукта: {item}')
#             continue
#         name = parts[0]
#         try:
#             prices = list(map(int, parts[1:]) if len(parts) > 1 else [])
#         except ValueError as e:
#             print(f'Ошибка при вводе цен для {name}: {e}')
#             continue
#         if prices:
#             average_price = sum(prices) / len(prices)
#             if average_price > limit:
#                 results.append(f'{name},{average_price:.1f}')
#     if results:
#         return sorted(results, key=sort_key)
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



# def solve(input_string: str) -> list:
#     # Преобразуем строку в список целых чисел.
#     try:
#         lst = list(map(int, input_string.split()))
#     except ValueError:
#         return ["Ошибка: неверный формат входных данных."]
#
#     # Проверяем, что длина списка не больше 100.
#     if len(lst) < 2 or len(lst) > 100:
#         return ["Ошибка: длина списка должна быть от 1 до 100."]
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


# 2 варианта использования цикла for :
# lst = [1, 2, 9, 8, 3, 4, 1, 2, 3, 4]
#
# longest_seq = []
# current_seq = []
#
# for i in range(len(lst)):
#     if not current_seq:
#         current_seq.append(lst[i])
#     else:
#         if lst[i] > current_seq[-1]:
#             current_seq.append(lst[i])
#         else:
#             if len(current_seq) > 1:
#                 longest_seq.append(current_seq)
#             current_seq = [lst[i]]
# if len(current_seq) > 1:
#     longest_seq.append(current_seq)
# for num in longest_seq:
#     print(' '.join(map(str, num)))

#



# или:
# lst = [1, 2, 9, 8, 3, 4, 1, 2, 3, 4]
#
# longest_seq = []
# current_seq = []
#
# for i in lst:
#     if not current_seq:
#         current_seq.append(i)
#     else:
#         if i > current_seq[-1]:
#             current_seq.append(i)
#         else:
#             if len(current_seq) > 1:
#                 longest_seq.append(current_seq)
#             current_seq = [i]
# if len(current_seq) > 1:
#     longest_seq.append(current_seq)
# for num in longest_seq:
#     print(' '.join(map(str, num)))



# напечатать индексы в строке:
# lst = [1, 2, 9, 8, 3, 4, 1, 2, 3, 4]
# indexes = ''
#
# for i in range(len(lst)):
#     indexes += str(i)
# print(' '.join(indexes.strip()))

# или:
# lst = [1, 2, 9, 8, 3, 4, 1, 2, 3, 4]
# indexes = [str(i) for i in range(len(lst))]
# print(' '.join(indexes))



#
#
# def split_into_increasing_sublists(lst):
#     # Проверяем, не пуст ли список
#     if not lst:
#         return []
#
#     sublists = []
#     current_sublist = []
#     for i in lst:
#         if not current_sublist:
#             current_sublist.append(i)
#         else:
#             if i > current_sublist[-1]:
#                 current_sublist.append(i)
#             else:
#                 if len(current_sublist) > 1:
#                     sublists.append(current_sublist)
#                 current_sublist = [i]
#
#     if len(current_sublist) > 1:
#         sublists.append(current_sublist)
#
#     return [' '.join(map(str, sequence)) for sequence in sublists]




# class PointDistanceCalculator:
#     def __init__(self, input_string):
#         if not input_string.strip():
#             raise ValueError('Error: Empty data')
#
#         try:
#             lst_points = [int(i) for i in input_string.split()]
#         except ValueError:
#             raise ValueError('Error: Enter integers')
#
#         if len(lst_points) != 4:
#             raise ValueError('Error: Enter 4 numbers')
#
#         self.x1, self.y1, self.x2, self.y2 = lst_points
#
#     def calculate_distance(self):
#         import math
#         distance = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
#         return f'{distance:.2f}'
#
#
# data_input = input()
# try:
#     calculate = PointDistanceCalculator(data_input)
#     print(calculate.calculate_distance())
# except ValueError as e:
#     print(e)




# class PointDistanceCalculator:
#     def __init__(self, input_string):
#         # Разделяем входящую строку по пробелам
#         lst = input_string.split()
#         if len(lst) != 4:
#             raise ValueError('Введите ровно 4 числа')
#
#         # Пробуем преобразовать строки в целые числа
#
#             # Сначала преобразуем в целые числа
#         try:
#             self.x1, self.y1, self.x2, self.y2 = map(int, lst)
#         except ValueError as e:
#             raise ValueError('Ошибка: Введите целые числа') from e
#
#     def calculate_distance(self):
#        import math
#        distance = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
#        return round(distance, 2)
#
#
# input_string = input()
# calculator = PointDistanceCalculator(input_string)
# print(calculator.calculate_distance())


# class PointDistanceCalculator:
#     def __init__(self, input_string):
#         lst = input_string.split()
#         if len(lst) != 4:
#             raise ValueError("Необходимо ввести ровно четыре числа, разделенные пробелами.")
#         try:
#             self.x1 = int(lst[0])
#             self.y1 = int(lst[1])
#             self.x2 = int(lst[2])
#             self.y2 = int(lst[3])
#         except ValueError:
#             raise ValueError("Все вводимые значения должны быть  целыми  числами.")
#
#     def calculate_distance(self):
#         import math
#         distance = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
#         return round(distance, 2)
#
# input_string = input()
# calculator = PointDistanceCalculator(input_string)
# print(calculator.calculate_distance())

# class PointDistanceCalculator:
#     def __init__(self, input_string):
#         lst = input_string.split()
#         if len(lst) != 4:
#             raise ValueError('Ошибка: Введите 4 числа')
#         try:
#             self.x1 = int(lst[0])
#             self.y1 = int(lst[1])
#             self.x2 = int(lst[2])
#             self.y2 = int(lst[3])
#         except ValueError:
#             raise ValueError('Ошибка: Введите целые числа: положительные, отрицательные или 0')
#         if not (self._are_coordinates_valid(self.x1, self.y1, self.x2, self.y2)):
#             raise ValueError('Ошибка: Введите целые числа: положительные, отрицательные или 0')
#
#     def _are_coordinates_valid(self, *coordinates):
#         return all(isinstance(coord, int) for coord in coordinates)
#     def calculate_distance(self):
#         import math
#         distance = math.sqrt((self.x2 - self.x1) ** 2 + (self.y2 - self.y1) ** 2)
#         return round(distance, 2)
#
#
# data_input = '0 1 0 0 '
# calculator = PointDistanceCalculator(data_input)
# print(calculator.calculate_distance())

