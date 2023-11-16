# # for x in 'hello':
# #     print(x.upper())
# #
# # for y in [1, 2, 3, 4]:
# #     print(y **2)
#
# # for num1 in range(10):
# #     for num2 in range(10):
# #         for num3 in range(10):
# #             for num4 in range(10):
# #                 print(num1, num2, num3, num4)
#
# squares = []
# cubes = []
# for num in range(101):
#     squares.append(([num, num ** 2, num **3]))
#     cubes.append((num, num ** 3))
# print(squares)
#
# for pair in squares:
#     print(f'Square of {pair[0]} is {pair[1]}')

# people = (['Jack', 'Smith', 25], ['Mary', 'Gold', 20], ['Bob', 'Dylan', 45])
# for name, surname, age in people:
#     result = f'Hello {name} {surname}. You are {age} years old.'
#     if age < 18:
#         result += ' You are teenager.'
# else:1
#         result += 'You are adult.'
# print(result)

# x = 0
# while x < 100:
#     print(x)
#     x +=1

# step_len = 0.8
# current_position = 0
# total_steps = 0
# distance_to_target = float(input('How many km you want to travel: ')) * 1000
# while current_position < distance_to_target:
#     current_position += step_len
#     total_steps += 1
#
# print(total_steps)
#
# x = 0
# while True:
#     if x > 10:
#         break
#     print(x)
#     x += 1
#
# for letter in 'python':
#     if letter == 'h':
#         continue
#     elif letter == 'n':
#         break
#     print(letter)

# user_choice = input('Please ')
# if user_choice == '1':
#     pass
# elif user_choice == '2'
#     pass

#38803160272
while True:
    user_input = input('Please enter ID code or type "exit": ')
    if user_input.lower() == 'exit':
        break
    try:
        int(user_input)
        if len(user_input) != 11:
            raise UserWarning
    except ValueError:
        print('ID code is not numeric!')
    except UserWarning:
        if len(user_input) > 11:
            print('Code is too long!')
        else:
            print('Code is too short!')
    else:
        while True:
            user_choice = input('Please choose\n'
                                '1.Gender\n'
                                '2.Date of birth\n'  #dd.mm.yyyy
                                '3.Region\n'
                                '4.Validate\n'
                                '5.Change ID\n'
                                '0.Exit\n'
                                '--> ')
            if user_choice == '1':
                if user_input[0] not in '09':
                    if int(user_input[0]) % 2 == 0:
                        print('You are female!')
                    else:
                        print('You are male!')
            elif user_choice == '2':
                f_year = user_input[1] + user_input[2]
                year = '19' + f_year
                day = user_input[5] + user_input[6]
                f_month = user_input[3] + user_input[4]
                print(day + ':' + f_month + ':' + year)
            elif user_choice == '3':
                pass
            elif user_choice == '4':
                pass
            elif user_choice == '5':
                break
            elif user_choice == '0':
                quit()
            else:
                print('Choise is out of range!')
