"""
Set
Sets are used to store multiple items in a single variable.

Set is one of 4 built-in data types in Python used to store

Collections of data, the other 3 are List, Tuple, and Dictionary, all with different qualities and usage.

A set is a collection which is both unordered and unindexed.

Sets are written with curly brackets.
-------------------------
STARTING WITH A EMPTY SET 
ADDING ONE set AT A TIME
"""
# Note: Sets are unordered, so you cannot be sure in which order the items will appear.

# CREATE EMPTY SET
empty_s1 = set() 
print(empty_s1)

# ADD A SET
empty_s1.add('COLLECTION_1')
print('THIS CRAZY EASY!', empty_s1)

# ADD ANOTHER SET
empty_s1.add('COLLECTION_2')
print('YOU CAN DO THIS TOO!', empty_s1)

# ADD ANOTHER SET
empty_s1.add('COLLECTION_3')
print("IT'S LIKE ", empty_s1, sep='-')

# 
"""
THIS IS THE OUTPUT
set()
THIS CRAZY EASY! {'COLLECTION_1'}
YOU CAN DO THIS TOO! {'COLLECTION_2', 'COLLECTION_1'}
"""



















