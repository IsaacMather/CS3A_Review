# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import numpy as np
import unittest

#list iterators
def list_iterators():
    #if it's a list, it will stay ordered
    fruits = ["Apple", "Banana", "Cherry"]

    for fruit in fruits:
        print(fruit)


    #if it's a set, the order is not guaranteed
    fruits = {"Apple", "Banana", "Cherry"}
    for fruit in fruits:
        print(fruit)


#custom execptions
class TooHighNumberError(Exception): #inherited class from the exception
# class, it's adopted all the methods and attributes of the exceptions class
    def __init__(self, message):
        self.message = message
#custom exceptions
def factorial(base: int):
    if base < 0:
        raise TooHighNumberError("Okease use a non-negative integer for base")
    result = 1
    for i in range(base + 1, 0, -1):
        result *= i
    return result


#mutable object trap
def append_first_letter(string: str, list_to_append=None):
    if list_to_append == None:
        list_to_append = []
    list_to_append.append(string[0])
    return list_to_append


#numpy arrays
def numpy_arrays():
    #you can't have ragged arrays in numpy
    #arrays have to be homogenious
    #arrays and lists are mutable
    #difference between an array and a list is in slicing
    #slice of a list is a new list, slice of an array is just a view in to
    # the array
    #with a list you can make a change to the slice, and the original list
    # is not affected


    a = np.array([[1, 2, 3], [4, 5, 6]], dtype=float)
    print(a)
    # print(a[0, 0])
    # print(a.dtype)
    # print(a.shape)
    # a = np.zeros((2, 3))
    # print(a)
    # b = np.ones((5, 5))
    # print(b)
    # c = np.arange(2, 20, 2)
    # print(c)
    # c = np.arange(20)
    # print(c)
    # c = c.reshape((4, 5))
    # print(c.shape)
    # print(c)
    #
    #slicing
    #first row and all the columns

    #slice of a list is a new list, while the slice of the array is just a
    # view, so you can make changes to the slice of the list and it will not
    # change the original list
    # slice = a[0:1, :]
    # print(f"slice is {slice}")
    #
    # #list slicing
    # a_list = [[1, 2, 3], [4, 5, 6]]
    # b_list = a_list[0][:]
    # print(b_list)
    # b_list[0] = 100
    # print(f"a_list {a_list}")
    # print(f"b_list {b_list}")
    a = np.random.random((5,5))
    a = np.random.randint(0, 1000, (4, 5))
    print(a)
    a = np.array([[1, 2, 3], [4, 5, 6]])
    #multiply an array by a scalar
    b = a * 4
    print(f"b is {b}")

    #you can add arrays
    b = a + a

    #you can multiply arrays
    b = a * a

    #you can do something called broadcasting
    b = a + 1 #this adds the number to every element in the array
    b = a + [1, 2, 3] #basically the items gets added to
    #broadcasting describes how NumPy treats arrays with different shapes
    # during arithmetic operations.

    #you can also sum all of the rows or the columns
    b = a.sum(axis=0)
    b = a.sum(axis=1)


def features_and_lables_of_neural_networks():
    #an example is one row of data
    #examples contain feeatures and possibly a label
    #features are used to apptempt to categorize the example
    #the label is the correct category that the example belongs to
    #features are the items that the machine learning algorithm has access
    # to, that is uses to predict the single label
    pass


#class method and static method decorators
class Dog:

    number_of_dogs = 0

    def __init__(self, name: str):
        print(f"{name} is born!")
        self._name = name
        self._location = "the doghouse"
        Dog.number_of_dogs += 1

    @classmethod
    def how_many_dogs(cls):
        return cls.number_of_dogs

    @staticmethod
    def how_many_legs(number_of_dogs: int):
        return number_of_dogs * 4

    @property
    def name(self):
        return self._name

    def bark(self):
        """Make fido talk"""
        print(f"{self._name} says woof!")

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, location: str):
        if location == "the kitchen" or location == "the doghouse":
            self._location = location
        else:
            raise ValueError


#properties and decorators?
def properties():
    #properties allow things to be called directly
    #they are still functions
    my_dog = Dog("fido")
    my_dog.location = "the kitchen"
    print(f"{my_dog.name} is in {my_dog.location}")


class TestCC(unittest.TestCase):
    def test_bad_currencies(self):
        with self.assertRaises(KeyError):
            cc.currency_converter(10, "AQD", "NZD")
        with self.assertRaises(KeyError):
            cc.currency_converter(10, "USD", "OZD")

    def test_non_positive_qty(self):
        with self.assertRaises(ValueError):
            cc.currency_converter(-1, "USD", "NZD")

    def test_return_value(self):
        self.assertEqual(8, cc.currency_converter(10, "USD", "HKD"))
        self.assertAlmostEqual(.71, cc.currency_converter(1, "CAD", "USD"), 2)
        self.assertEqual(2.8, cc.currency_converter(1.8, "EUR", "USD"))
        self.

def pythons_built_in_unittest_package():

    pass


def xor():
    #featuyres and labels of exclusive or
    #exclusive or is true only if one of the inputs is true, so therefore
    features =  [[0, 0], [1, 0], [0, 1], [1, 1]]
    labels = [[0], [1], [1], [0]]
    #we are going to use this in our mahcine learning algo to help train our
    # model?

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # #list iteraots
    # list_iterators()
    #
    # #custom exceptions
    # print(factorial(5))
    # try:
    #     print(factorial(-1))
    # except TooHighNumberError as problem:
    #     print(problem.message)
    #
    # #class and static methods
    # dog_one = Dog("fido")
    # print(dog_one.name)
    # dog_one.talk
    # print(f"there are {dog_one.how_many_dogs()} dogs in the universse")
    # dog_two = Dog("Fifi")
    # print(f"there are {dog_two.how_many_dogs()} dogs in the universse")
    # dog_legs = Dog.how_many_legs(Dog.how_many_dogs())
    # print(f"There are {dog_legs} dog legs in the universe")
    #
    # # mutable object trap
    # my_list = ["a", "b"]
    # append_first_letter("cat", my_list)
    # print(my_list)
    # my_new_list = append_first_letter("dog")
    # print(my_new_list)
    # my_newer_list = append_first_letter("elephant")
    # print(my_newer_list)
    # numpy_arrays()
    # features_and_lables_of_neural_networks()
    # pythons_built_in_unittest_package()
    properties()
    xor()