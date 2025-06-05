# import sys
#
# sys.argv = ['scrypt.py', 'test_arg1', 'test_arg2']
#
# print("This is the name of the program:", sys.argv[0])
#
# print("Argument List:", str(sys.argv))




# import sys

# def main():
#     # Первый элемент sys.argv — это имя скрипта
#     script_name = sys.argv[0]
#     # Остальные элементы — это аргументы, переданные скрипту
#
#     arguments = ['arg1', 'arg2']
#     print(f"Имя скрипта: {script_name}")
#     print(f"Аргументы: {arguments}")
#
# if __name__ == "__main__":
#     main()



# import sys

# sys.argv = ['scrypt.py', 'test_arg1', 'test_arg2']
# def print_args():
#     for i, arg in enumerate(sys.argv):
#         print(f'Argument {i}: {arg}')
# print_args()


# import csv
#
# input_file_path = './Orders_etl.csv'
# output_file_path = './output.csv'
#
# # Множество для хранения уникальных строк
# unique_rows = set()
#
# # Чтение из CSV файла
# with open(input_file_path, mode='r', newline='', encoding='utf-8') as input_file:
#     reader = csv.DictReader(input_file)
#     # Получаем заголовки столбцов
#     fieldnames = reader.fieldnames
#     print(fieldnames)
#
#     # Перебираем строки
#     for row in reader:
#         # Превращаем строку в кортеж для создания уникального идентификатора
#         row_tuple = tuple(row.items())
#         print(row_tuple)
#         unique_rows.add(row_tuple)  # Добавляем кортеж в множество для удаления дубликатов
#
# # Запись уникальных строк в новый CSV файл
# with open(output_file_path, mode='w', newline='', encoding='utf-8') as output_file:
#     writer = csv.DictWriter(output_file, fieldnames=fieldnames)
#
#     # Записываем заголовки
#     writer.writeheader()
#
#     # Перебираем уникальные строки и записываем их
#     for row_tuple in unique_rows:
#         # Превращаем кортеж обратно в словарь
#         row_dict = dict(row_tuple)
#         writer.writerow(row_dict)
#
# print("Уникальные строки успешно записаны в файл:", output_file_path)


# import csv
#
# input_file_path = 'data.csv'
# with open(input_file_path, 'w', newline='', encoding='utf-8') as input_file:
#     writer = csv.writer(input_file)
#     writer.writerow(['name', 'city'])
#     writer.writerow(['Oleg', 'Moscow'])
#     writer.writerow(['Bob', 'London'])
#
# with open(input_file_path, 'r', newline='', encoding='utf-8') as output_file:
#     reader = csv.reader(output_file)
#     for row in reader:
#         print(' '.join(map(str, row)))


# import re
#
# strings = ['123hello', 'abcde', 'HelloWorld123', 'a1b2c3d4e5f6', 'aBcD1']
#
# for s in strings:
#     res = re.findall(r'(?=.*[a-z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z].*[a-zA-Z])', s)
#     if res:
#         print(f'"{s}": yes')
#     else:
#         print(f'"{s}": no')


# def count_vowels_and_consonants(text: str):
#     count_vowels = 0
#     count_consonants = 0
#     lower_text = text.lower()
#     if len(lower_text) < 1 or len(lower_text) > 100:
#         return 'Invalid input'
#     punctuation = "!-,.? "
#     clean_text = lower_text.translate(str.maketrans('', '', punctuation))
#     vowels = set('ауоиэыяюеё')
#     for letter in clean_text:
#         if letter in vowels:
#             count_vowels += 1
#         elif letter.isalpha():
#             count_consonants += 1
#     return count_vowels, count_consonants
#
# input_string = input()
# vowels, consonants = count_vowels_and_consonants(input_string)
# print(vowels, consonants)




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


# import re
#
# def count_vowels_and_consonants(text: str):
#     count_vowels = 0
#     count_consonants = 0
#     if not (1 <= len(text) <= 100):
#         return 'Invalid input'
#     clean_text = re.sub(r'[^а-яА-ЯёЁ]', '', text.lower())
#     vowels = 'ауоиэыяюеё'
#     for letter in clean_text:
#         if letter in vowels:
#             count_vowels += 1
#         else:
#             count_consonants += 1
#     return count_vowels, count_consonants
#
#
# data_input = input()
# vowels, consonants = count_vowels_and_consonants(data_input)
# print(vowels, consonants)



# import re
#
# def count_vowels_and_consonants(text: str):
#     if len(text) == 0 or not (1 <= len(text) <= 100):
#         raise ValueError('Invalid input')
#     count_vowels = 0
#     count_consonants = 0
#     lower_text = text.lower()
#     clean_text = re.sub(r'[^а-яА-ЯёЁ]', '', lower_text)
#     vowels_in_text = set('ауоиэыяюеё')
#     for letter in clean_text:
#         if letter in vowels_in_text:
#             count_vowels += 1
#         else:
#             count_consonants += 1
#     return count_vowels, count_consonants
#
#
# data_input = input()
# try:
#     vowels, consonants = count_vowels_and_consonants(data_input)
#     print(vowels, consonants)
# except TypeError as e:
#     print(e)



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



# data_input = input()
# blocks = data_input.split('|')
# if not (1 <= len(blocks) <= 100):
#     raise ValueError('Invalid Input')
# products_dict = {}
# results = []
# for block in blocks:
#     try:
#         parts = block.split(',')
#         if len(parts) != 3:
#             raise ValueError(f'Invalid block format: {block}. Expected "name, category, price"')
#         name, category, price = parts
#         try:
#             price = float(price)
#         except ValueError:
#             raise ValueError(f'"{price}" must be number')
#         if category not in products_dict:
#             products_dict[category] = []
#         products_dict[category].append((name, price))
#     except ValueError as e:
#         print(e)
#         continue
# for category, items in products_dict.items():
#     items.sort(key=lambda x: (x[1], x[0]))
#     results.append(f'{category}:')
#     for item in items:
#         results.append(f'{item[0]},{item[1]}')
#
# for result in results:
#     print(result)




# def solve(string):
#     res = []
#     limit = 30
#
#     for line in string.split('|'):
#         name, price = line.split(',')
#         name = name.strip()
#         price = float(price.strip())
#         if (name, price) not in res:
#             res.append((name, price))
#     sub_res = [(name, price) for name, price in res if price > limit]
#     sub_res.sort(key=lambda x: (x[1], x[0]))
#     total = [f'{name} {price}' for name, price in sub_res]
#     return '\n'.join(total)
#
#
#
#
# data = 'яблоки,23|груши,34|бананы,45'
# print(solve(data))



# def solve(string):
#     res = []
#     limit = 30
#     for line in string.split('|'):
#         parts = line.split(',')
#         name = parts[0]
#         prices = []
#         for price_str in parts[1:]:
#             try:
#                 price = int(price_str.strip())
#                 prices.append(price)
#             except ValueError:
#                 print(f"Ошибка: невозможно преобразовать '{price_str}' в число. Пропускаем")
#                 continue
#         if prices:
#             average_price = sum(prices) / len(prices)
#             if average_price > limit:
#                 prices.sort()
#                 res.append((name, prices))
#     res.sort(key=lambda x: (sum(x[1]) / len(x[1]), x[0]), reverse=True)
#     total = [f'{name} {' '.join(map(str, prices))}' for name, prices in res]
#     return '\n'.join(total)
#
#
#
# data = 'яблоки,23,25|груши,45,60|бананы,39,34'
# print(solve(data))




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




# import re
#
# string = '''
# My emails: valid.email@example.com or another_valid-email@subdomain.example.net
# or 12345@example.org or user456@mail.ru or user123@example.com or example.com or user@
# or @domain.com or user@mail.rf
# '''
#
# email_regex = r'\b[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.(?:ru|com|net|org)\b'
# #email_regex = r'\b[a-zA-Z0-9.\-_]+@[a-zA-Z0-9.-]+\.(?:ru|com|net|org)\b' #экранируем "-" если в середине[]
# emails = re.findall(email_regex, string)
# print(emails)




# import re
#
# string = '''My emails: valid.email@example.com or another_valid-email@subdomain.example.net
#     or 12345@example.org or invalid-email or invalid.email@example or .invalid@example.com
#     or invalid.@example.com or test.email@example.museum or test.email@example.comextra
#     or user123@example.com or user456@mail.ru or _invalid@example.com and -invalid@example.com
# '''
# email_regex = r'\b(?<![._-])[a-zA-Z0-9][a-zA-Z0-9._-]*[^.]@[a-zA-Z0-9.-]+\.(?:ru|com|net|org)\b'
# emails = re.findall(email_regex, string)
# print('\n'.join(emails))