# 'r' - read
# 'a' - append
# 'w' - write
# 'x' - create
# 'r+' - read and write

# file = open('lor.txt', 'r', encoding='utf-8')
# print(file.name)
# print(file.mode)
# print(file.encoding)
# file.close()
# print(file.closed)

# with open('lor.txt', 'r', encoding='utf-8') as file:
#     # file_content = file.readlines()
#     # file_content = file.readline()
#       file_content = file.read(20)
#       print(file_content)
#       file_content = file.read(20)
#       print(file_content)
#
#     # file_content = file.read()
#
#
#
# print(file_content)
# print(type(file_content))
# print(len(file_content))

# with open('lor.txt', 'r', encoding='utf-8') as file:
#     read_size = 100
#     file_content = file.read(read_size)
#     file.write('Hello world!')

# with open('lor_copy.txt', 'w', encoding='UTF-8') as file:
#      file.write('Hi There\n')
#      file.write('Hello World\n')
#      file.write(input('Enter name: '))


# with open('lor_copy.txt', 'x', encoding='UTF-8') as file:
#     file.write('Hi There\n')
#     file.write('Hello World\n')
#     file.write(input('Enter name: \n'))

# with open('lor_copy.txt', 'r+', encoding='UTF-8') as file:
#     data = file.read().upper()
#     file.write(data)

with open('icon.png', 'rb') as picture:
    data = picture.read()


with open('logo.jpg', 'wb') as picture_copy:
    picture_copy.write(data)

print(data)

