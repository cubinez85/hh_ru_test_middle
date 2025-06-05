# def max_sequence_sum(numbers: str, sequence_length: str) -> str:
#     try:
#         lst_numbers = list(map(int, numbers.split()))
#         length = int(sequence_length)
#     except ValueError:
#         return 'Введите целые числа'
#
#     if length > len(lst_numbers):
#         return 'Invalid input'
#     if length < 1:
#         return 'Введите положительное число'
#     is_increasing_positive = all(lst_numbers[i] < lst_numbers[i+1] for i in range(len(lst_numbers)-1)) and all(num > 0 for num in lst_numbers)
#     is_decreasing_negative = all(lst_numbers[i] > lst_numbers[i+1] for i in range(len(lst_numbers)-1)) and all(num < 0 for num in lst_numbers)
#     if not (is_increasing_positive or is_decreasing_negative):
#         return "Последовательность должна быть строго возрастающей положительной или строго убывающей отрицательной"
#
#     if is_increasing_positive:
#         return str(sum(lst_numbers[-length:]))
#     else:
#         return str(sum(lst_numbers[:length]))
#
#
# numbers_list = input()
# sequence_length = input()
# result = max_sequence_sum(numbers_list, sequence_length)
# print(result)



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



# class MyInt(int):
#     pass
#
#
# x = MyInt(5)
# print(isinstance(x, int))
# print(type(x) is int)
# print(x is type(int))



# def count_nums(string_input):
#     positive_numbers = 0
#     negative_numbers = 0
#     zero_count = 0
#     try:
#         lst = list(map(int, string_input.split()))
#         if len(lst) > 100:
#             return 'Длина списка не больше 100 элементов'
#         for num in lst:
#             if num > 0:
#                 positive_numbers += 1
#             elif num < 0:
#                 negative_numbers += 1
#             else:
#                 zero_count += 1
#     except ValueError:
#         return 'Введите целые числа'
#     return f'выше нуля: {positive_numbers}, ниже нуля: {negative_numbers}, равна нулю: {zero_count}'
#
#
# data_input = input()
# result = count_nums(data_input)
# if result is not None:
#     print(result)


# def process(input_string: str) -> str:
#     positive_nums = 0
#     negative_nums = 0
#     zero_nums = 0
#     try:
#         numbers = input_string.split()
#         if len(numbers) > 100:
#             return 'Ошибка: Длина списка не более 100 элементов'
#         for i in numbers:
#             if not i.strip():
#                 continue
#             num = int(i)
#             if num > 0:
#                 positive_nums += 1
#             elif num < 0:
#                 negative_nums += 1
#             else:
#                 zero_nums += 1
#         res1 = str(positive_nums)
#         res2 = str(negative_nums)
#         res3 = str(zero_nums)
#         return f'выше нуля: {res1}, ниже нуля: {res2}, равна нулю: {res3}'
#     except ValueError:
#         return 'Ошибка: Введите целые числа'
#
#
# input_string = input()
# output_string = process(input_string)
# print(output_string)