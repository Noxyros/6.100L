"""
Recursion is a programming technique where a function solves a problem by calling itself with a smaller input.
It breaks complex problems into simpler sub-problems and requires a base case (to stop execution) and
a recursive case (to move closer to the base case) (Divide and Conquer)
"""

# Exercise 1
# Complete the function that calculates np for variables n and p
"""
Power of some number is basically that number multiplied by itself p times.
For example 2^3 or 2**3 is equal to 2*2*2 = 8.
by that logic n to the power of p is n^p = n*n*n*n... so we can say n^p = n * (p -1).
"""


# Answer 1
# def power_recur(n: int, p: int) -> int:
#     if p == 0:
#         return 1
#     else:
#         return n * power_recur(n, p-1)
#
# print(power_recur(2, 3))


# Exercise 2
# Modify the code we wrote to return the total length of all strings inside L:
# def total_len_recur(L: list) -> int:
#     if len(L) == 1:
#         return _______
#     else:
#         return __________________
#
# test = ["ab", "c", "defgh"]
# print(total_recur(test)) # prints 8


# Answer 2
# def total_len_recur(L: list) -> int:
#     if len(L) == 1:
#         return len(L[0])
#     else:
#         return len(L[0]) + total_len_recur(L[1:])
#
# test = ["ab", "c", "defgh"]
# print(total_len_recur(test)) # prints 8


# Exercise 3
# def in_list_of_lists(L: list, e:int) -> bool:
#     """
#     L is a list whose elements are lists containing ints.
#     Returns True if e is an element within the lists of L
#     and False otherwise.
#     """
#
# test = [[1,2], [3,4], [5,6,7]]
# print(in_list_of_lists(test, 0)) # prints False
# test = [[1,2], [3,4], [5,6,7]]
# print(in_list_of_lists(test, 3)) # prints True

# Answer 3
# def in_list_of_lists(L, e):
#     if not L:
#         return False
#     elif e in L[0]:
#         return True
#     else:
#         return in_list_of_lists(L[1:], e)
#
#
# test = [[5,6,7]]
# print(in_list_of_lists(test, 0)) # prints False
# test = [[1,2], [3,4], [5,6,7]]
# print(in_list_of_lists(test, 9)) # prints True


# def my_rev(L):
# #     if not L:
# #         return []
# #     elif len(L) == 1:
# #         return L
# #     else:
# #         print(L[0])
# #         print(L)
# #         return my_rev(L[1:]) + [L[0]]
# #
# # test = [1,2,3,4]
# # print(my_rev(test))