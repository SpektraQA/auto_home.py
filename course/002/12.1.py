import itertools

# counter = itertools.count()
# data = [100, 200, 300, 400, 500]
# data2 = [5, 6, 7, 8, 9, 10, 11, 12, 13]
#
# print(list(itertools.zip_longest(data, data2, counter)))

# counter = itertools.count(start=10, step=-5)

# counter = itertools.repeat(3)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))

# letters = ['a', 'b', 'c', 'd']
# numbers = [1, 2, 3, 4]
# numbers2 = [4, 5, 4, 3, 2, 1, 0, 4]
# selectors = [True, False, False, True]
# names = ['Jack', 'Mary']
#
# # result = itertools.dropwhile(lambda x: x>2, numbers2)
# # result = itertools.takewhile(lambda x: x> 2, numbers2)
# # print(list(result))
#
# # result = itertools.compress(letters, numbers)
# # print(list(result))
# #
# # result = itertools.filterfalse(lambda x: x>2, numbers)
# # print(list(result))
# # result2 = filter(lambda x: x>2, numbers2)
# # print(list(result2))
# # #No ORDER NO REPEAT
# # result = itertools.combinations(range(10), 3)
# #ORDER, NO REPEAT
# # result = itertools.permutations(letters, 2)
# #ORDER, REPEAT
# # result = itertools.product(letters, repeat=4)
# #NO ORDER, REPEAT
# # result = itertools.combinations_with_replacement(letters, 4)
#
# # for c in result:
# #     print(c)
#
# result = itertools.accumulate(numbers2)
# print(list(result))


people = [
    {
        'name': 'John Smith',
        'city': 'Berlin'
    },
    {
        'name': 'Mary Gold',
        'city': 'Berlin'
    },
    {
        'name': 'Taavi Tamm',
        'city': 'Berlin'
    },
    {
        'name': 'Piere Cardin',
        'city': 'Tallinn'
    },
    {
        'name': 'Jack Rock',
        'city': 'Tallinn'
    },
    {
        'name': 'Lee Hong',
        'city': 'Tallinn'
    },
    {
        'name': 'Abdul Faruh',
        'city': 'Dubai'
    },
    {
        'name': 'Mary Pierce',
        'city': 'Dubai'
    },
    {
        'name': 'Lee Hong',
        'city': 'Tallinn'
    }
]
people.sort(key=lambda x: x['city'])
result = itertools.groupby(people, lambda x: x['city'])
print(list(result))

for key, group in result:
    print(list(group))