numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def squares(number):
    return number **2

new_nums = map(squares, numbers)

# new_nums = []
# for num in numbers:
#     new_nums.append(squares(num))
#
print(list(new_nums))

def change_dict(d):
    make, model, serial = d['make'], d['model'], d['serial']
#     return {
#         serial: {
#             'make': make,
#             'model':model
#         }
#     }
#
#
# cars = [
#     {
#         'make': 'VW',
#         'model': 'Golf',
#         'serial': '2123cnzxmdsdksad'
#     },
#     {
#         'make': 'BMW',
#         'model': '320i',
#         'serial': '777773cnzxmd777ad'
#     },
#     {
#         'make': 'Seat',
#         'model': 'Leon',
#         'serial': '9999hhhh99999'
#     }
# ]
#
# new_cars = map(change_dict, cars)
# print(list(new_cars))

def power(a,b):
    return a*b
nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [5, 6, 7, 8, 9, 10]

new = map(power, nums1, nums2)
print(list(new))

# def odd_or_even(number):
#     if number % 2 ==0:
#         return True
#     else:
#         return False
#
# new = filter(odd_or_even, nums1)
# print(list(new))

# data1 = [1, 2, 3, 4, 5]
# data2 = ['mon', 'tue', 'wed', 'thu', 'fri']
#
# new = zip(data1, data2)
# print(list(new))
