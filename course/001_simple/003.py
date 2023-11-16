# # import string
# #
# # symbols = str.maketrans('', '', string.punctuation)
# # print(string.punctuation)
# x = 0
#
# if x > 0:
#     print('X is greater than zero')
# elif x < 0:
#     print('X is smaller than zero')
# else:
#     print('X is equal to zero')
# idcode = '12345678912'
#
# if len(idcode) ==11:
#     print('OK')
# elif len(idcode) > 11:
#     print('TOO LONG')
# else:
#     print('TOO SHORT')

# name = 'Samantha'
# if len(name) > 5 and len(name) < 10:
#     print(name)
# print(not True)
# print(not 1)
# print(not'')
#
# if not name == 'Sam':
#     print('OK')

# if 'x' not in 'hello world':
#     print('OK')

# empty = []
# empty = list()
# print(type(empty))
# print(bool(empty))

# world = 'world'
#
# filled_list = [12312, 123.1231, 'Hello', world, [1, [4, 5, 6], 3]]
# print(len(filled_list))
# print(filled_list[-1][1][2] ** 2)
# courses = ['History', 'Programming', 'Math', 'Literature', 'Physics', 'art', 'english']
# numbers = [1, 5, 6, 8, 3, 4, 2]

# test = [1, 2, 3]
# test[1] = 777
# print(test)

# courses.append('English')
# courses.insert(1, 'Art')
# courses.extend(['english', 'art'])
# print(courses)
# courses.remove('Math')
# removed = courses.pop(1)
# print(removed)
# courses.reverse()
# courses.sort(reverse=True)
# print(courses)
# numbers.sort()
# print(numbers)

# print(min(courses))
# print(max(courses))
# print(sum(numbers))
# print('Math' in courses)
#
# courses_str = ', '.join(courses)
# print(courses_str)
# print(str(courses))

# print('hello world'.split('l'))

# a = 10
# b = a.copy
# a +=20
# print(a, b)

# courses = ('History', 'Programming', 'Math', 'Literature', 'Physics', 'art', 'english')
# numbers = (1, 5, 6, 8, 3, 4, 2)

courses = {'History', 'Programming', 'Math', 'Literature', 'Physics', 'art', 'english', 'Math'}
numbers = {1, 5, 6, 8, 3, 4, 2}

# empty = set()
# print(type(empty))
#
# print(courses)
# courses.remove('Math')
# print(numbers)

# set1 = {'Math', 'History', 'Programming', 'Physics'}
# set2 = {'Art', 'Physics', 'Design', 'History'}
# set3 = {'Art', 'Design'}
# print(set1.intersection(set2))
#
# print(set1.difference(set2))
# print(set2.difference(set1))
#
# print(set3.issubset(set2))
# print(set2.issuperset(set3))

# print(list(range(10, 20, 2)))

for number in range(101):
    if number % 2 ==0:
        print(number)

