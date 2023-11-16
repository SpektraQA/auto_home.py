import re

# text = '#KLS323', #423abc, #AABBPP, #AAABBBCCCC
# hex_color = re.compile(r'#\b[0-9a-fA-F]{6}\b')
#
# matches = re.finditer(hex_color, text)
# for match in matches:
#     print(match)

# text = '"2*9-6*5'" or (3+5)-9*4"
# hex_color = re.compile(r'#\b[0-9a-fA-F]{6}\b')
# plus_numbers = re.compile(r'(\d)([^+])')
#
# matches = re.finditer(hex_color, text)
# for match in matches:
#     print(match)

text = '123:123'
hex_color = re.compile(r'#\b[0-9a-fA-F]{6}\b')
plus_numbers = re.compile(r'(\d)([^+])')
time_pattern = re.compile(r'\b[01]\d|2[0-3]):([0-5]\d)\b')
matches = re.finditer(hex_color, text)
address_pattern = re.compile(r'\d{3} [A-Za-z0-9-]+ St\., [A-Za-z- \']+ [A-Z]{2} \d{5}')
name_pattern = re.compile(r'\b[01]\d|2[0-3]):([0-5]\d)\b')
idcode = re.compile(r'[1-8]\d\d(0[1-9]|1[0-2])(0[1-9]|[12][0-9]|3[01])\d{4}')


people = []
people_matches = re.findall(name_pattern, data)
address_matches = re.findall(address_pattern, data)
print(len(people_matches))
for person in people_matches:
    print(person)