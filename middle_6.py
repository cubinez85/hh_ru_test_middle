# order_ids = set()
#
# order_ids.add('Order234')
# order_ids.add('Order489')
# order_ids.add('Order234')
# print(', '.join(map(str, order_ids)))


# def solve(street_dark, office_full):
#     if street_dark and office_full:
#         return 'light on'
#     else:
#         return 'light off'
#
#
# street_dark = False
# office_full = False
# print(solve(street_dark, office_full))


# class Light:
#     def __init__(self):
#         self.power_on = False
#         self.street_dark = True
#         self.office_full = True
#     def toggle_power(self):
#         if self.street_dark and self.office_full:
#             self.power_on = not self.power_on
#             return 'Light on'
#         else:
#             self.power_on = False
#             return 'Light off'
#
#
# my_light = Light()
# print(my_light.toggle_power())


# class Light:
#     @staticmethod
#     def toggle_power(street_dark, office_full):
#         if street_dark and office_full:
#             return 'Light on'
#         else:
#             return 'Light off'
#
#
# street_dark = True
# office_full = True
# print(Light.toggle_power(street_dark, office_full))


# class Light:
#     def __init__(self):
#         self.power_on = False
#     def toggle_power(self, street_dark, office_full):
#         if street_dark and office_full:
#             self.power_on = not self.power_on
#             if self.power_on:
#                 return 'Light on'
#             else:
#                 return None
#         else:
#             return 'Light off'
#
#
# street_dark = False
# office_full = True
# my_light = Light()
# print(my_light.toggle_power(street_dark, office_full))


# class Light:
#     power_on = False
#     @classmethod
#     def toggle_power(cls, street_dark, office_full):
#         if street_dark and office_full:
#             cls.power_on = not cls.power_on
#             if cls.power_on:
#                 return 'Light on'
#             else:
#                 return None
#         else:
#             return 'Light off'
#
#
# street_dark = True
# office_full = True
# print(Light.toggle_power(street_dark, office_full))


# def func(element, *args):
#     return args.count(element)
# print(func(2, 1, 2, 3, 2))
# print(func(1, 2, 2, 1))


# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
#
# info(name='cubinez85', age=60, city='Moscow')


# def info(**kwargs):
#     for key, value in kwargs.items():
#         print(f'{key}: {value}')
#
#
# info(name='Oleg', age=60, city='Moscow')
#
#
# def greet(name, greeting='Hello', **kwargs):
#     print(f'{greeting}, {name}!')
#     if kwargs:
#         print('Дополнительная информация: ')
#         info(**kwargs)
#
#
# greet('Bob', status='single', occupation='programmer')


# import time
#
#
# class Smartphone:
#     def __init__(self):
#         self.bluetooth = True
#         self.target = 7
#
#     def toggle_bluetooth(self):
#         if self.target % 2 == 0:
#             self.bluetooth = not self.bluetooth
#             if self.bluetooth:
#                 return 'bluetooth on'
#             else:
#                 return 'bluetooth off'
#         else:
#             print('Задержка 5 секунд ...')
#             time.sleep(5)
#             self.bluetooth = self.bluetooth
#             if self.bluetooth:
#                 return 'bluetooth on'
#             else:
#                 return 'bluetooth off'
#
#
# my_phone = Smartphone()
# print(f'Начальное состояние Bluetooth: {my_phone.bluetooth}')
# print(my_phone.toggle_bluetooth())
# print(f'Конечное состояние Bluetooth: {my_phone.bluetooth}')
# my_phone.target = 8
# print(f'Новое значение Target: {my_phone.target}')
# print(my_phone.toggle_bluetooth())
# print(f'Состояние Bluetooth после смены Target: {my_phone.bluetooth}')



# import datetime
#
# current_time = datetime.datetime.now()
# print(current_time.strftime('%d-%m-%Y %H:%M:%S'))


# import re
#
# string = '123'
# res = re.findall(r'^(?!0)\d+$', string)
# print(res)