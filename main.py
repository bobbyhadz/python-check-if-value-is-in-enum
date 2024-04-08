# Check if a value exists in an Enum in Python

from enum import Enum


class Sizes(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3


values = [member.value for member in Sizes]
print(values)  # 👉️ [1, 2, 3]

if 2 in values:
    # 👇️ this runs
    print('2 is in enum values')
else:
    print('2 is NOT in enum values')

print(100 in values) # 👉️ False