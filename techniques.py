"""
Purpose:
    contain all methods based in functional concept: first-class function.
Methods:
    1) closure [x]
    2) partial function [x]
    3) currying []
    4) composition function [x]
"""
from functools import *


# closure
def sum_with_five_without_closure(value, unmodified_value=5):
    return unmodified_value + value


def sum_with_five_with_closure():
    unmodified_value = 5

    def sum(value):
        return unmodified_value + value
    return sum


# partial function
def function_1(line):
    return '\t'.join(line.split(" "))


def function_2(line):
    return '\n'.join(line.split(" "))


def abstract_function(line, delimiter):
    return delimiter.join(line.split(" "))


tab_delimiter_process = partial(abstract_function, delimiter='\t')


# composition function
sum = lambda x : x + 1
power_double = lambda x : x*x
divide_by_2 = lambda x : x/2


def composition_manual_1(x):
    return sum(divide_by_2(power_double(x)))


def composition_manual_2(x):
    y = power_double(x)
    y = divide_by_2(y)
    return sum(y)


# the composition is the right side
def composition_function(*functions):
    return reduce(lambda f, g: lambda x: g(f(x)), functions, lambda x: x)


# the composition is the right side
def composition_function_revert(*functions):
    return reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)


composition_automatic = composition_function(power_double, divide_by_2, sum)
composition_automatic_revert = composition_function_revert(sum, divide_by_2, power_double)

#currying


# main
# partial function
print("using partial function")
print(function_1("hola que tal"))
print(abstract_function("hola que tal", '\t'))
print(tab_delimiter_process("hola que tal"))

# composition function
print("using composition function")
print(composition_manual_1(6))
print(composition_manual_2(6))
print(composition_automatic(6))
print(composition_automatic_revert(6))

# closure
print("using closure")
print(sum_with_five_without_closure(5))
print(sum_with_five_with_closure()(5))

