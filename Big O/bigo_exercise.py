import time
import math
# from functools import wraps

# -------------------------------------------------- #
# EXAMPLE: timing a program
# -------------------------------------------------- #

# def time_wrapper(f):
#     # Helper function to show timing
#     @wraps(f)
#     def wrapper(*args, **kwargs):
#         print('Input:', args[0])
#         t = time.time()
#         result = f(*args, **kwargs)
#         dt = time.time() - t
#         print(f"{f.__name__} took {dt:.8f} sec")
#         return result
#     return wrapper
#
#
# @time_wrapper
# def c_t_f(c):
#     # Constant time
#     return c * 9.0 / 5 + 32
#
#
# @time_wrapper
# def summation(x):
#     # Linear time
#     total = 0
#     for e in range(x + 1):
#         total += e
#     return total
#
#
# @time_wrapper
# def square(n):
#     # Quadratic time
#     sqsum = 0
#     for i in range(n):
#         for j in range(n):
#             sqsum += 1
#     return sqsum
#
#
# # Creating a list
# L = [1]
# for k in range(9):
#     L.append(L[-1] * 10)
#
# for val in L:
#     # temp_f = c_t_f(val)
#     # mysum = summation(val)
#     square(val)


# -------------------------------------------------- #
# EXAMPLE: counting the number of operations
# -------------------------------------------------- #

# def count_wrapper(f, l):
#     print('Counting', f.__name__)
#     for i in l:
#         counter = f(i)[0]
#         if i == min(l):
#             multiplier = 1.0
#         else:
#             multiplier = counter/float(prev)
#         prev = counter
#         print(f"{f.__name__}({i}): {counter} ops, {round(multiplier, 5)} x more")
#
# def c_to_f(c):
#     counter = 3
#     return counter, c * 9.0/5 + 32
#
# def mysum(x):
#     counter = 1
#     total = 0
#     for i in range(x):
#         counter += 3
#         total += i
#     return counter, total
#
# def square(n):
#     counter = 1
#     total = 0
#     for i in range(n):
#         counter += 1
#         for j in range(n):
#             counter += 3
#             total += 1
#     return counter, total
#
# L1 = [100]
# for e in range(5):
#     L1.append(L1[-1] * 10)
#
# L2_a = [128, 256, 512, 1024, 2048, 4096, 8192]
# L2_b = [1, 10, 100, 1000, 10000]

# count_wrapper(c_to_f, L1)
# count_wrapper(mysum, L1)
# count_wrapper(square, L2_a)
# count_wrapper(square, L2_b)

# ---------------------------------------------------------------------------------------------------------------------

# def time_wrapper(f, L):
#     print("Timing:", f.__name__)
#     for i in L:
#         print("Input:", i)
#         t0 = time.perf_counter()
#         result = f(i)
#         dt = time.perf_counter() - t0
#         print(f"Took about {dt:.20f} to run")
#
# def convert_to_km(m):
#     return m * 1.609
#
#
# my_list = [1]
# for x in range(5):
#     my_list.append(my_list[-1]*10)
#
# time_wrapper(convert_to_km, my_list)

