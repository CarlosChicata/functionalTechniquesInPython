"""
Purpose:
    contain all methods based in functional concept: first-class function.
Methods:
    1) closure [x]
    2) partial function [x]
    3) currying
    4) composition function
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


# main
print(function_1("hola que tal"))
print(abstract_function("hola que tal", '\t'))
print(tab_delimiter_process("hola que tal"))
