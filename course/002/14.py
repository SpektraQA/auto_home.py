# import re
#
# # Sample string
# text_to_search = '''
# abcdefghijklmnopqurtuvwxyz
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 1234567890
# Ha HaHa HaHaHa
# MetaCharacters (Need to be escaped):
# . ^ $ * + ? { } [ ] \ | ( )
# example.com
# 321-555-4321
# 123.555.1234
# 123*555*1234
# 800-555-1234
# 900-555-1234
# Mr. Jones
# Mr Smith
# Ms Davis
# Mrs. Robinson
# Mr. T
# abc
# ball mall hall wall tall
# '''
#
# sentence = 'Start a sentence and then bring it to an end'
#
# emails = '''
# SampleMaiL@example.com
# john.sample@my-work.net
# jack-125-production@colledge.edu
# bob.Samples@example.co.uk
# example@example.org
# '''
#
# urls = '''
# https://www.google.com
# http://www.wordpress.org
# https://www.nasa.gov
# https://example.net
# www.example.net
# example.net
# '''
#
# pattern = re.compile(r'(abc)(def)(ghi)')
#
# matches = pattern.finditer(urls)
# for match in matches:
#     # print(match)
#     print(match.group(4))
#     # print(match.start(), match.end(), match.span(), match.group())




# # Backslash t will insert space in front of Tab string (this is formatted string)
# print('\tTab')
#
# # For Regular Expressions we need to give raw string. r is used in front of a string
# print(r'\tTab')
#
#
# # # Example of simple pattern #
# pattern = re.compile(r'abc')
# # pattern = re.compile(r'bca')  # Example of a no match raw string
#
# # Finditer method creates an iterable object with all matches
# matches = pattern.finditer(text_to_search)
#
# # For loop to gather all matches from finditer result
# for match in matches:
#     print(match)
#
# # Result
# # <re.Match object; span=(1, 4), match='abc'>
# # span=(1, 4) are indexes from 1 to 4 where match was found
#
# # Sliced string, span values show where abc match occurs in string
# print(text_to_search[1:4])
# print(text_to_search[264:267])
#
# # Get span values
# for match in matches:
#   print(match.start(), match.end(), match.group())
#
# # Data type of matches variable
# print(type(matches))
#
# # Data type of match variable
# print(type(match))
#
#
#
# # Characters that need to be escaped #
#
# # pattern = re.compile(r'.')  # Not escaped period
# # pattern = re.compile(r'\.')  # Escaped period
# # pattern = re.compile(r'example\.com')  # URL sample, escaped period
#
# matches = pattern.finditer(text_to_search)
# for match in matches:
#     print(matc

