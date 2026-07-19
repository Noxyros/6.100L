# Exercise 1

# def keys_with_value(aDict, target):
#     """
#     aDict: a dictionary
#     target: an integer or string
#     Assume that keys and values in aDict are integers or strings.
#     Returns a sorted list of the keys in aDict with the value target.
#     If aDict does not contain the value target, returns an empty list.
#     """
#     # Your code here
#
# # Examples:
# aDict = {1:2, 2:4, 5:2}
# target = 2
# print(keys_with_value(aDict, target)) # prints the list [1,5]

# Answer 1
# def keys_with_value(aDict, target):
#     result = []
#     for k in aDict:
#         if aDict.get(k) == target:
#             result.append(k)
#     result.sort()
#     return result
#
# Dict = {5:2, 2:4, 1:2}
# Dict = {"Daniel":"Pig", "Yohan":"God", "Suma":"Pig"}
# Target = 2
# Target = "Pig"
# print(keys_with_value(Dict, Target)) # prints the list [1,5]


# Exercise 2
# def all_positive(d):
#     """
#     d is a dictionary that maps int:list
#     Suppose an element in d is a key k mapping to value v (a non-empty list).
#     Returns the sorted list of all k whose v elements sums up to a
#     positive value.
#     """
#     # Your code here
#
# # Examples:
# d = {5:[2,-4], 2:[1,2,3], 1:[2]}
# print(all_positive(d))   # prints the list [1, 2]

# # Answer 2
# def all_positive(d):
#     result = []
#     for k,v in d.items():
#         if sum(v) >= 0:
#             result.append(k)
#     result.sort()
#     return result
#
# d_1 = {5:[2,-4], 2:[1,2,3], 1:[2]}
# print(all_positive(d_1))   # prints the list [1, 2]