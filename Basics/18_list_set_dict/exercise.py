"""
1. Create a Dictionary which contains the Binary values mapping with numbers found in the below integer and binary and save it in binary_dict.

"""
integer = [0 , 1, 2, 3, 4]
binary = ['0', '1', '10', '11', '100']
binary_dict = {k: v for k, v in zip(integer, binary)}
print("Binary dictionary:", binary_dict)


"""
2. Create a List which contains additive inverse of a given integer list. An additive inverse a for an integer i is a number such that:
a + i = 0
"""
integer_list = [1, -1, 2, 3, 5, 0, -7]
additive_inverse = [-i  for i in integer_list]
print("Additive inverse of the integer list:", additive_inverse)


"""
3. Create a set which only contains unique squares from a given a integer list.
"""
integer = [1, -1, 2, -2, 3, -3]
squares_set = {i ** 2 for i in integer}
print("Unique squares set:", squares_set)

