# x = 5
# x = (x + 1) ** ((x > 5) + 1)  # x > 5 = False = 0
# print(x)



# class C:
#     def __init__(self):
#         self.x = []
#         self.y = []
#
#     def f(self, a, b):
#         self.x.append(a)
#         self.y.append(b)
#
#     def g(self, a):
#         for i in range(len(self.x)):
#             if self.x[i] == a:  # проверяем каждый элемент списка
#                 return self.y[i]
#         return None
#
#
# c = C()
# c.f(1, 'one')
# c.f(2, 'two')
# print(c.g(2))


# for i in range(0, 10):
#     if i % 2 == 0:
#         continue
#     else:
#         print(i, end='')


# def f(a):
#     def g():
#         nonlocal a
#         print(a, end='')
#         a += 1
#     return g
#
#
# g_inner = f(10)
# g_inner()
# g_inner()


# class Cat:
#     def __init__(self, striped, age, color):
#         self.striped = striped
#         self.age = age
#         self.color = color
#
#
# my_cat = Cat(True, 3, 'black')
# print(my_cat.striped)


# n = 4
# matrix = [[i + j * n + 1 for i in range(n)] for j in range(n - 1, -1, -1)]
# for row in matrix:
#     print(row)


# n = 4
# matrix = [[i * n + j + 1 for i in range(n)] for j in range(n - 1, -1, -1)]  #ответ на задание
# for row in matrix:
#     print(row)


# n = 4
# matrix = [[i * n + j + 1 for i in range(n)] for j in range(0, n)]
# for row in matrix:
#     print(row)


# n = 4
# matrix = [[i + j * n + 1 for i in range(n - 1, -1, -1)] for j in range(n - 1, -1, -1)]
# for row in matrix:
#     print(row)


# n = 4
# matrix = [[i + j * n for i in range(n)] for j in range(n - 1, -1, -1)]
# for row in matrix:
#     print(row)


# n = 4
# result = []
# for j in range(n - 1, -1, -1):  # Внешний цикл (j убывает)
#     row = []
#     for i in range(n):  # Внутренний цикл (i возрастает)
#         value = i + j * n + 1
#         row.append(value)
#     result.append(row)
#
# for row in result:
#     print(row)


# with open('file_system_test.txt', 'a') as test:
#     for i in range(0, 5):
#         test.write(str(i))
#     test.write('test passed')


# import os
# import shutil
#
# path_to_dir = './test_dir_for_rm'
# if os.path.exists(path_to_dir):
#     try:
#         shutil.rmtree(path_to_dir)
#         print(f'Директория: "{path_to_dir}" успешно удалена')
#     except OSError as e:
#         print(f'Ошибка при удалении директории: "{path_to_dir}": {e}')
# else:
#     print(f'Директория: "{path_to_dir}" не существует')


# import re
# string = 'AfThj'
# result = re.findall(r'^[a-zA-z]{5}', string)
# print(result)


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


# def select_candidates(candidate_strings):
#     if not candidate_strings:
#         return ['Error: Empty data']
#     if not (2 <= len(candidate_strings) <= 100):
#         return ['Error: Length strings of candidates is out of range (2,100)']
#     surnames = [block.split(',')[0] for block in candidate_strings]
#     if len(surnames) != len(set(surnames)):
#         return ['Error: All surnames must be unique']
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