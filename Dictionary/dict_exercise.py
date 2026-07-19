"""
A compound data type is a data type made up of multiple values grouped together.
A compound data type acts as a container. It can hold simple, single value (Scalars like 1 or "Hungry") or even another
containers (like tuple or another list). For example [1, "Hungry", ('x', 3.5)].
"""

# d = {"Ana":'B', "Matt":'C', "John": 'B', "Katy":'A'}

# Exercise 1

# def find_grades(grades, students):
# """
#   grades is a dict mapping student names (str) to grades (str)
#   students is a list of student names
#   Returns a list containing the grades for students (in same order)
# """
# # for example
# d = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}
# print(find_grades(d, ['Matt', 'Katy'])) # returns ['C', 'A']

# Answer 1

# def find_grades(grades, students):
#
#     """
#     Find some value in dictionary entry using iteration on iterable data.
#     Students can be scalar or any compound data type including dictionary.
#     If composite then Students are not the key!!! It's just an iterable object containing our key that mapped to certain value.
#     """
#
#     if len(students) > 1 and not isinstance(students, str):
#         # Using list comprehension -> More pythonic and clear, name is a string like "Matt" or "Katty".
#         # Name acts as a key to retrieve an entry value.
#         # Iterating students (in this case a list). Each iteration, var name have single string value.
#         # Using .get() method to avoid programming crash. If key doesn't exist, then return None or set return value manually.
#         return [grades.get(name, "Null") for name in students]
#     else:
#         # If the students is less than 2 and is an instance of a string then execute this instead.
#         return grades.get(students)
#
# print(find_grades(d, ["Matt", "Katty"]))
# print(find_grades(d, "Anna"))

# d["Yohan"] = 'A' # Add an entry.
# print(d)
#
# d["Yohan"] = 'A+' # Edit an entry.
# print(d)
#
# del d["Matt"]
# # Delete an entry, can also use pop (my_dict.pop(key, optional return value if the key is not in dict)).
# # Can safe the .pop() method return values on a variable.
# print(d)
#
# # Check if key is in dictionary using keyword "in".
# print("Yohan" in d)
# print("Helel" in d)

# Exercise 2

# def find_in_L(Ld, k):
# """ Ld is a list of dicts
# k is an int
# Returns True if k is a key in any dicts of Ld and False otherwise """
# # for example
# d1 = {1:2, 3:4, 5:6}
# d2 = {2:4, 4:6}
# d3 = {1:1, 3:9, 4:16, 5:25}
# print(find_in_L([d1, d2, d3], 2) # returns True
# print(find_in_L([d1, d2, d3], 25) # returns False

# Answer 2

# def find_in_L(Ld, k):
#     for d in Ld: # d is a dictionary like d1, d2, and d3
#         if k in d:
#             return True
#     return False
#
# d1 = {1:2, 3:4, 5:6}
# d2 = {2:4, 4:6}
# d3 = {1:1, 3:9, 4:16, 5:25}
# print(find_in_L([d1, d2, d3], 2)) # returns True
# print(find_in_L([d1, d2, d3], 25)) # returns False

# test_list = {'Ana':'B', 'Matt':'C', 'John':'B', 'Katy':'A'}

# """
# Can get keys out of dictionary using .keys() method.
# In the newest python, order is the same as the order when the data is inserted.
# DO NOT ASSUME IT IS ORDERED!
# For example if the keys is an int, when we retrieve it and cast/convert it into a list, the order will not be sorted.
# {3:3, 2:1, 9:2} when cast to list, still going to be [3, 2, 9] unless do sorted() function on it.
# """
# print(list(test_list.keys())) # Cast to a list to make it more recognizable (optional)
#
# print(list(test_list.values())) # Can look for values instead
#
# print(list(test_list.items())) # Or key-value pair

# Typical use is to iterate over items (key-value)
# for k, v in test_list.items():
#     print(f"Key {k} has Value {v}")


# Exercise 3
# def count_matches(d):
# """ d is a dict
# Returns how many entries in d have the key equal to its value """
# # for example
# d = {1:2, 3:4, 5:6}
# print(count_matches(d)) # prints 0
# d = {1:2, 'a':'a', 5:5}
# print(count_matches(d)) # prints 2

# Answer 3
# def count_matches(d):
#     result = 0
#     for k, v in d.items():
#         if k == v:
#             result += 1
#     return result
#
# d1 = {1:2, 3:4, 5:6}
# print(count_matches(d1)) # prints 0
# d2 = {1:2, 'a':'a', 5:5}
# print(count_matches(d2)) # prints 2

# Exercise 4
# my_d ={'Ana':{'mq':[10], 'ps':[10,10]},
# 'Bob':{'ps':[7,8], 'mq':[8]},
# 'Eric':{'mq':[3], 'ps':[0]} }
# def get_average(data, what):
# all_data = []
# for stud in data.keys():
# INSERT LINE HERE
# return sum(all_data)/len(all_data)

# Answer 4
# def get_average(data, what):
#     all_data = []
#     for stud in data:
#         all_data += data[stud][what]
#     return sum(all_data)/len(all_data)
# print(get_average(my_d, 'mq'))

# Final
# song = "RAH RAH AH AH AH ROM MAH RO MAH MAH"
#
# def generate_word_dict(music):
#     song_low  = music.lower()
#     words_l = song_low.split()
#     word_dict  = {}
#     for w in words_l:
#         if w in word_dict:
#             word_dict[w] += 1
#         else:
#             word_dict[w] = 1
#     return word_dict
#
#
# diction = generate_word_dict(song)
#
# def frequent_word(d):
#     l = []
#     highest = max(d.values())
#     for k,v in d.items():
#         if v == highest:
#             l.append(k)
#     return l, highest
#
# common = frequent_word(diction)
#
# def occurs_often(d, x):
#     freq_l = []
#     word_freq_tuple = frequent_word(d)
#     while word_freq_tuple[1] > x:
#         freq_l.append(word_freq_tuple)
#         for word in word_freq_tuple[0]:
#             del(d[word])
#         word_freq_tuple = frequent_word(d)
#     return freq_l
#
# print(occurs_often(diction, 1))