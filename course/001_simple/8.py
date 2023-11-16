# def no_parameter():
# #     print('Hello World!')
# #
# # no_parameter()
# #
# return 'Hello world!'
#
# print(no_parameter())
# x = no_parameter()
# print(x)

# def with_params(a):
#     print(a ** 2)
# with_params(10)
#
# def odd_or_even(number):
#     # if number % 2 == 0:
#     #     return 'Odd'
#     # else:
#     #     return 'Even'
#     if number ==7:
#         return number ** 2
#     pass
# print(odd_or_even(1))

# x = [1, 2, 3, 4, 5, 6]
#
# for num in x:
#     print(f'{num} is {odd_or_even(num)} number')
#
# print(range(10))

# def say_hello(first_name, last_name):
#     print(f'Hello {first_name} {last_name}')
# first = input('Enter name: ')
# last = input('Enter lastname: ')
# print(say_hello(first, last))
#
# def sum_three_or_two(num1, num2, num3=0, *args, **kwargs):
#     print(args)
#     return num1 + num2 + num3
# #
# x = sum_three_or_two(3, 4, 0, 1, 2, 4, 'asd', 'weq')
# print(x)

# x = sum_three_or_two()

# def tester(num1, num2, num3):
#     print(num1, num2, num3)
# tester(1, 2, 3)
# tester(num3=1,num2=2,num1=3)

# a = 1
# b = 2
# c = 3
#
# def tester():
#     a = 10
#     b = 20
#     c = 30
#     print(a, b, c)
#
# tester()
# print(a, b, c)

# import helpers
#
# print(helpers.sqrt(144))
# print(helpers.format_name('serhii', 'PEREDERIIEV'))

# from helpers import rectangle_area
# print(rectangle_area(10, 20))

def hello():
    print('Hello')


    def wrapper():
        hello()
        hello()

        wrapper()