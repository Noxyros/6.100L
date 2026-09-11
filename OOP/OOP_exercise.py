import math
import random


#
# class Coordinate(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def distance(self, other):
#         x_diff_distance = (self.x - other.x)**2
#         y_diff_distance = (self.y - other.y)**2
#         return math.sqrt(x_diff_distance + y_diff_distance)
#
#     def to_origin(self):
#         self.x = 0
#         self.y = 0
#         return self.x, self.y
#
#     def get_val(self):
#         return self.x, self.y
#
#     def set_val(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"<{self.x}, {self.y}>"
#
# class Circle(object):
#     def __init__(self, center: Coordinate, radius: int):
#         assert isinstance(center, Coordinate) and isinstance(radius, int), "Invalid Value!!!"
#         self.c = center
#         self.r = radius
#
#     def circumference(self):
#         return 2*math.pi*self.r
#
#     def area(self):
#         return (math.pi*self.r)**2
#
#     def is_inside(self, point):
#         return point.distance(self.c) < self.r
#
#     def is_inside2(self, point):
#         return self.c.distance(point) < self.r
#
#
# # YES WE CAN
# # cen = Coordinate(2, 2)
# # circle_1 = Circle(cen, 2)
# # print(circle_1)
# # print(circle_1.c.y)
#
#
# p1 = Coordinate(2, 2)
# p2 = Coordinate(5, 8)
# p3 = Coordinate(1, 1)
# my_circle = Circle(p1, 2)
# print(my_circle.is_inside(p3))
# print(my_circle.is_inside2(p3))
#
#
# class Fraction(object):
#     def __init__(self, n, d):
#         self.num = n
#         self.denom = d
#
#     def times(self, other):
#         top = self.num * other.num
#         bottom = self.denom * other.denom
#         return f"{top}/{bottom} = {top/bottom}"
#
#     def plus(self, other):
#         top = (self.num * other.denom) + (self.denom * other.num)
#         bottom = self.denom * other.denom
#         return f"{top}/{bottom} = {top/bottom}"
#
#     def minus(self, other):
#         top = (self.num * other.denom) - (self.denom * other.num)
#         bottom = self.denom * other.denom
#         return f"{top}/{bottom} = {top/bottom}"
#
#     def get_inverse(self):
#         return f"{self.denom}/{self.num} = {self.denom/self.num}"
#
#     def invert(self):
#         self.num, self.denom = self.denom, self.num
#
#     def __str__(self):
#         if self.denom == 1:
#             return f"{self.num}/{1}"
#         elif self.denom == 0:
#             raise Exception("Error: Division by zero!")
#         else:
#             return f"{self.num}/{self.denom}"
#
#     def __mul__(self, other):
#         top = self.num * other.num
#         bottom = self.denom * other.denom
#         return Fraction(top, bottom)
#
#     def __float__(self):
#         return self.num/self.denom
#
#     def reduce(self):
#         def gcd(n, d):
#             while d != 0:
#                 (n, d) = (d, n%d)
#             return n
#         if self.denom == 0:
#             raise ZeroDivisionError("Fraction denominator cannot be zero!")
#         elif self.denom == 1:
#             return Fraction(self.num, 1)
#         else:
#             divisor = gcd(self.num, self.denom)
#             return Fraction(self.num // divisor, self.denom // divisor)

# frac_1 = Fraction(3, 4)
# frac_2 = Fraction(2, 2)
# # print(frac_1.mult(frac_2))
# print(frac_1.plus(frac_2))
# print(frac_1.minus(frac_2))
#
# f1 = Fraction(3,4)
# print(f1.get_inverse()) # prints 1.33333333 (note this one returns value)
# f1.invert() # acts on data attributes internally, no return
# print(f1.num, f1.denom)
#
# c = Coordinate(3, 4)
# print(c)
# print(type(c))
# print(isinstance(c, Coordinate))
#
# a = Fraction(1,4)
# b = Fraction(3,1)
# print(a) # prints 1/4
# print(b) # prints 3
#
# a = Fraction(1,4)
# b = Fraction(2,3)
# print(a)
# c = a * b
# print(c)
# print(float(c))
# print(c.reduce())
#
# f1 = Fraction(5,1)
# f2 = Fraction(2,5)
# f3 = f1 * f2
# print(type(f3.reduce()))
# print(type(Fraction.__str__(f3)))

# t = Fraction(2, 12)
# print(t.reduce())


class Animal():
    def __init__(self, name, age):
        self.years = age
        self.name = name

    def __str__(self):
        return f"{self.name} : {self.years}"

    def get_age(self):
        return self.years

    def get_name(self):
        return self.name


def make_animals(L1, L2):
    L3 = []
    for i in range(len(L1)):
        L3.append(str(Animal(L1[i], L2[i])))
    return L3


# L1 = [2,5,1]
# L2 = ["blobfish", "crazyant", "parafox"]
# animals = make_animals(L1, L2)
# print(animals)
#
# for i in animals:
#     print(i)

class Cat(Animal):
    def speak(self):
        print("Meow...")

    def __str__(self):
        return f"Cat:{self.name}:{self.years}"


class Person(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.friends = []

    def get_friends(self):
        return self.friends.copy()

    def add_friends(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)

    def speak(self):
        print("Hello...")

    def age_diff(self, other):
        diff = self.years - other.years
        print(abs(diff), "year difference!")

    def __str__(self):
        return f"Person:{self.name}:{self.years}"


def make_pets(d):
    for k, v in d.items():  # items return an iterable object key-value pair
        # k is a person, v is a cat
        print(k.get_name() + ':' + v.get_name())

    # Alternative if wanna iterate using just 1 pointer
    # for k in d:
    #     print(k.get_name()+':'+d[k].get_name())


# p1 = Person("ana", 86)
# p2 = Person("james", 7)
# c1 = Cat("furball", 1)
# c2 = Cat("fluffsphere", 1)
# d = {p1: c1, p2: c2}
# make_pets(d)

# p1.age_diff(p2)

# class Student(Person):
#     def __init__(self, name, age, major=None):
#         super().__init__(name, age)
#         self.major = major
#
#     def change_major(self, major):
#         self.major = major
#
#     def speak(self):
#         r = random.random()
#         if r < 0.25:
#             print("I have homework")
#         elif 0.25 <= r < 0.5:
#             print("I need sleep")
#         elif 0.5 <= r < 0.75:
#             print("I should eat")
#         else:
#             print("I'm still zooming")
#
#     def __str__(self):
#         return f"Student:{self.name}:{self.age}:{self.years}"


from dateutil import parser

class Workout():
    call_per_hour = 200

    def __init__(self, start, end, calories=None):
        self.start = parser.parse(start)
        self.end = parser.parse(end)
        self.calories = calories
        self.icon = '😰'
        self.kind = 'Workout'

    def get_calories(self):
        if self.calories == None:
            return Workout.call_per_hour*(self.end-self.start).total_seconds()/3600
        else:
            return self.calories

    def get_start(self):
        return self.start

    def get_end(self):
        return self.end

    def set_calories(self, calories):
        self.calories = calories

    def set_start(self, start):
        self.start = start

    def set_end(self, end):
        self.end = end

w_one = Workout("1/1/2021 3:30 PM", "1/1/2021 4:00 PM")
print(w_one.get_calories())
w_two = Workout("1/1/2021 3:35 PM", "1/1/2021 3:35 PM", 300)
print(w_two.get_calories())