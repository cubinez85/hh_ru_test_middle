# def func(a, b=[]):
#     b.append(a)
#     return b
# func(1)
# print(func(2, [10, 20]))
# print(func(3))


# def func(a, b=None):
#     if b is None:
#         b = []
#     b.append(a)
#     return b
#
#
# print(func(1))
# print(func(2, [10, 20]))
# print(func(3))


# def horizontal(board, player):
#     for row in board:
#         if row[0] == player or row[1] == player or row[2] == player:
#             return True
#     return False
#
#
# board = [
#     ['X', 'O', 'X'],
#     ['O', 'X', 'X'],
#     [' ', ' ', 'O']
# ]

# if horizontal(board, 'X'):
#     print("Игрок X выиграл")



# def horizontal(board, player):
#     for row in board:
#         if row.count(player) == 3:
#             return True
#     return False
# board = [
#     ['X', 'O', 'X'],
#     ['X', 'X', 'X'],
#     [' ', ' ', 'O']
# ]
#
# if horizontal(board, 'X'):
#     print('Игрок Х выиграл')
# else:
#     print('Игрок Х не выиграл')



# def horizontal(board, player):
#     # Проверяем только вторую строку (с индексом 1)
#     row = board[1]
#     return row.count(player) == 3  # Возвращаем True, если три знака игрока
#
# # Пример доски
# board = [
#     ['X', 'O', 'X'],
#     ['X', 'X', 'X'],  # Это вторая строка
#     [' ', ' ', 'O']
# ]
#
# if horizontal(board, 'X'):
#     print("Игрок X выиграл")
# else:
#     print("Игрок X не выиграл")



# numbers = [1, 2, 3, 4, 5]
# with open('numbers.txt', 'w') as file:
#     for number in numbers:
#         file.write(str(number))


# numbers = [1, 2, 3, 4, 5]
# with open('numbers.txt', 'w') as file:
#     file.write('\n'.join(str(number) for number in numbers))


# numbers = [1, 2, 3, 4, 5]
# with open('numbers.txt', 'w') as file:
#     for number in numbers:
#         file.write(str(number) + '\n')


# numbers = [1, 2, 3, 4, 5]
# with open('numbers.txt', 'w') as file:
#     for number in numbers:
#         file.write(str(number) + ' ')

# import os
# path = './'
# file_list = os.listdir(path)
# print(len(file_list))


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


# def solve(input_string: str) -> str:
#     if not input_string.split():
#         return 'Входная строка не может быть пустой'
#     try:
#         lst = list(map(int, input_string.split()))
#     except ValueError:
#         return 'Введите целые числа'
#     if len(lst) > 100:
#         return 'Длина списка не больше 100'
#
#     data_max = []
#
#     for i, value in enumerate(lst):
#         if i == 0:
#             data_max.append(value)
#         else:
#             data_max.append(max(value, data_max[-1]))
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
#         return ' '.join(safe_passwords) #элементы в списке safe_passwords уже являются строками
#
#
# input_string = input()
# check = CheckPasswords(input_string)
# print(check.solve())





# special_symbols = "!@#$%^&*()-+"
#
#
# class CheckPasswords:
#     def __init__(self, passwords):
#         self.passwords = passwords.split()
#
#     @staticmethod
#     def is_safe_password(password):
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
#     def solve(self):
#         if not (1 <= len(self.passwords) <= 100):
#             return 'Invalid input: Length self.passwords must be not more 100'
#         safe_passwords = [password for password in self.passwords if self.is_safe_password(password)]
#         return ' '.join(safe_passwords) if safe_passwords else 'Не найдено'
#
#
# input_string = input()
# try:
#     check = CheckPasswords(input_string)
#     print(check.solve())
# except ValueError as e:
#     print(e)





# special_symbols = "!@#$%^&*()-+"


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
#         return password
#     def solve(self):
#         if not (1 <= len(self.passwords) <= 100):
#             return 'Invalid input: Length self.passwords must be not more 100'
#         safe_passwords = [password for password in self.passwords if self.is_safe_password(password)]
#         if not safe_passwords:
#             return 'Не найдено'
#         return ' '.join(safe_passwords) #элементы в списке safe_passwords уже являются строками
#
#
#
# input_string = input()
# check = CheckPasswords(input_string)
# print(check.solve())



# class PasswordChecker:
#     @staticmethod
#     def is_safe_password(password):
#         special_symbols = "!@#$%^&*()-+"
#         if (len(password) < 8 or
#                 not any(char in special_symbols for char in password) or
#                 not any(char.isdigit() for char in password) or
#                 not any(char.isupper() for char in password) or
#                 not any(char.islower() for char in password)):
#             return False
#         return True
#     @staticmethod
#     def solve(input_string):
#         passwords = input_string.split()
#         if not (1 <= len(passwords) <= 100):
#             raise ValueError('Invalid input')
#         safe_passwords = [password for password in passwords if PasswordChecker.is_safe_password(password)]
#         return ' '.join(safe_passwords) if safe_passwords else 'Не найдено'
#
#
#
# data_input = input()
# print(PasswordChecker.solve(data_input))


# class PasswordChecker:
#     @staticmethod
#     def is_safe_password(password):
#         special_symbols = "!@#$%^&*()-+"
#         if not any(check in special_symbols for check in password):
#             return False
#         if not any(check.isdigit() for check in password):
#             return False
#         if not any(check.isupper() for check in password):
#             return False
#         if not any(check.islower() for check in password):
#             return False
#         return True
#
#
# input_string = input()
# safe_check = PasswordChecker.is_safe_password(input_string)
# print(safe_check)


# class PasswordChecker:
#     @staticmethod
#     def is_safe_password(password):
#         special_symbols = "!@#$%^&*()-+"
#         if not any(check in special_symbols for check in password):
#             return False
#         if not any(check.isdigit() for check in password):
#             return False
#         if not any(check.isupper() for check in password):
#             return False
#         if not any(check.islower() for check in password):
#             return False
#         return True
#
#     def solve(self, input_string):
#         if self.is_safe_password(input_string):
#             return ' '.join(input_string)
#         return 'Не найдено'
#
#
# data_input = input()
# safe_check = PasswordChecker()
# print(safe_check.solve(data_input))