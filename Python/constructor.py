"""
# Lab: Decorators

##### Goal

Write a Python Decorator that will tell us how long a function took to execute.

##### Instructions

Use pythons time module to calculate the time it took a function to execute.

"""


def wrapper_function(main_function):
    def wrapper():
        print("Some stuff before.")
        main_function()
        print("Some stuff after.")
    return wrapper

# @wrapper_function


def simple_function(*args):
    return sum(args)

wrapper_function()