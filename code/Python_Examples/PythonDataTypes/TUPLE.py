"""
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.
---------------------------
STARTING WITH A EMPTY TUPLE 
AN ADDING ANY DATA TYPE
"""
# created a empty tuple
empty_t1 = ()
print(type(empty_t1))
print(empty_t1)

# adding a tuple
add_to_tuple = list(empty_t1)
add_to_tuple.append("first_tuple")
switched_back_to_tuple = tuple(add_to_tuple)
print(switched_back_to_tuple)

# adding a tuple
add__next_tuple = list(empty_t1)
add__next_tuple.append("second_tuple")
switched_back_to_tuple = tuple(add__next_tuple)
print(switched_back_to_tuple)

# adding a tuple
add__next1_tuple = list(empty_t1)
add__next1_tuple.append("third_tuple")
switched_back_to_tuple = tuple(add__next1_tuple)
print(switched_back_to_tuple)
"""
THIS IS THE OUTPUT
<class 'tuple'>
()
('first_tuple',) 
('second_tuple',)
('third_tuple',)
"""
