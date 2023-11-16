import csv


# with open('test.csv', 'r') as file:
#     csv_reader = csv.reader(file)
#
#     # headers = next(csv_reader)
#     #
#     # for name, dob, city in csv_reader:
#     #     print(name, dob, city)
#
#     with open('test_copy.csv', 'w') as wfile:
#         csv_writer = csv.writer(wfile,
#                                 lineterminator = '\n',
#                                 delimiter='.',
#                                 # quotechar='r'
#                                 quoting = csv.QUOTE_ALL
#                                 )
#
#         for line in csv_reader:
#             csv_writer.writerow(line)
#
#
# with open('test_copy.csv', 'r') as new_file:
#     csv_reader = csv.reader(new_file, delimiter=',')
#
#     for line in csv_reader:
#         print(line)
