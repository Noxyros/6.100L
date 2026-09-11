# import math

# # Exercise 1
#
# class Circle:
#     def __init__(self, name: str, radius):
#         """ Initializes self with radius """
#         self.radius = radius
#         self.name = name
#
#     def get_radius(self):
#         """ Returns the radius of self """
#         return self.radius
#
#     def set_radius(self, radius):
#         """ radius is a number
#         Changes the radius of self to radius """
#         self.radius = radius
#
#     def get_area(self):
#         """ Returns the area of self using pi = 3.14 """
#         return round(math.pi * pow(self.radius, 2), 4)
#
#     def equal(self, c):
#         """ c is a Circle object
#         Returns True if self and c have the same radius value """
#         return self.radius == c.radius
#
#     def bigger(self, c):
#         """ c is a Circle object
#         Returns self or c, the Circle object with the bigger radius """
#         if self.radius > c.radius:
#             return f"{self.name} is bigger: {self.radius}"
#         elif self.radius < c.radius:
#             return f"{c.name} is bigger: {c.radius}"
#         else:
#             return f"{self.name} and {c.name} are equal: {c.radius}"
#
#
# other_circle = Circle("other_circle", 4)
# my_circle = Circle("my_circle", 5)
# print(my_circle.get_radius())
# print(my_circle.get_area())
# other_circle.set_radius(5)
# print(other_circle.get_radius())
# print(other_circle.equal(my_circle))
# print(my_circle.bigger(other_circle))
# print(Circle.equal(my_circle, other_circle))
# my_circle.set_radius(7)
# print(my_circle.bigger(other_circle))


# # Exercise 2
#
# class Circle:
#     def __init__(self, radius):
#         """ Initializes self with radius """
#         self.r = radius
#
#     def get_radius(self):
#         """ Returns the radius of self """
#         return self.r
#
#     def __add__(self, c):
#         """ c is a Circle object
#         Returns a new Circle object whose radius is
#         the sum of self and c's radius """
#         return Circle(self.r + c.r)
#
#     def __str__(self):
#         """ A Circle's string representation is the radius """
#         return f"This circle has radius of {self.r:.1f}"  # :.2f in an f-string is a format specifier.
#
# mc = Circle(2.7)
# oc = Circle(6.4)
# print(oc.get_radius())
# print(mc)
# print(mc + oc)  # print function immediately call the __str__ dunder method


# # Exercise 3

"""
In this problem, you will implement two classes according to the specification below: one Container class and one Stack class (a subclass of Container).
Our Container class will initialize an empty list. The two methods we will have are to calculate the size of the list and to add an element.
The second method will be inherited by the subclass. We now want to create a subclass so that we can add more functionality—the ability to remove elements from the list.
A Stack will add elements to the list in the same way, but will behave differently when removing an element.
A stack is a last-in, first-out data structure. Think of a stack of pancakes. As you make pancakes, you create a stack of them with older pancakes going on the bottom and newer pancakes on the top.
As you start eating the pancakes, you pick one off the top so, you are removing the newest pancake added to the stack. When implementing your Stack class, you will have to think about which end of your list contains the element that has been in the list the shortest amount of time. This is the element you will want to remove and return.
"""

# class Container:
#     """
#     A container object is a list and can store elements of any type
#     """
#     def __init__(self):
#         """
#         Initializes an empty list
#         """
#         self.L = []
#
#     def get_size(self):
#         """
#         Returns the length of the container list
#         """
#         return len(self.L)
#
#     def add_elem(self, e):
#         """
#         Adds the elem to one end of the container list, keeping the end
#         you add to consistent. Does not return anything
#         """
#         self.L.append(e)
#
# class Stack(Container):
#     """
#     A subclass of Container. Has an additional method to remove elements.
#     """
#     def rmv(self):
#         """
#         The newest element in the container list is removed
#         Returns the element removed or None if the queue contains no elements
#         """
#         if self.L:
#             return self.L.pop()
#         return None
#
# mc = Container()
# print(mc.get_size())
# mc.add_elem(5)
# mc.add_elem(6)
# print(mc.get_size())  # Can't use rmv method for container since it's only define inside the subclass
#
# ms = Stack()
# ms.add_elem("Fervent")
# ms.add_elem(3)
# print(ms.get_size())
# print(ms.rmv())
# print(ms.rmv())
# print(ms.rmv())


# # Exercise 4

"""
In this problem, you will implement two classes according to the specification below: one Container class and one Queue class (a subclass of Container).      
Our Container class will initialize an empty list. The two methods we will have are to calculate the size of the list and to add an element.
The second method will be inherited by the subclass. We now want to create a subclass so that we can add more functionality—the ability to remove elements from the list.
A Queue will add elements to the list in the same way, but will behave differently when removing an element.

A queue is a first-in, first-out data structure. Think of a store checkout queue. The customer who has been in the line the longest gets the next available cashier.
When implementing your Queue class, you will have to think about which end of your list contains the element that has been in the list the longest.
This is the element you will want to remove and return.
"""

# class Container(object):
#     """
#     A container object is a list and can store elements of any type
#     """
#     def __init__(self):
#         """
#         Initializes an empty list
#         """
#         self.myList = []
#
#     def size(self):
#         """
#         Returns the length of the container list
#         """
#         return len(self.myList)
#
#     def add(self, elem):
#         """
#         Adds the elem to one end of the container list, keeping the end
#         you add to consistent. Does not return anything
#         """
#         self.myList.append(elem)
#
# class Queue(Container):
#     """
#     A subclass of Container. Has an additional method to remove elements.
#     """
#     def remove(self):
#         """
#         The oldest element in the container list is removed
#         Returns the element removed or None if the stack contains no elements
#         """
#         if self.size() > 0:
#             return self.myList.pop(0)
#         return None
#
# mc = Container()
# print(mc.size())
# mc.add(5)
# mc.add(6)
# print(mc.size())  # Can't use remove method for container since it's only define inside the Queue subclass
#
# ms = Queue()
# ms.add("Fervent")
# ms.add(3)
# print(ms.size())
# print(ms.remove())
# print(ms.remove())
# print(ms.remove())
