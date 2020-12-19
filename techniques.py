"""
Purpose:
    contain all methods based in functional concept: first-class function.
Methods:
    1) closure [x]
    2) partial function [x]
    3) currying [x]
    4) composition function [x]
    5) complex example using severan funcion []
"""
from functools import *
from collections import Counter


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


# currying
def without_currying(a, b, c):
    return a + b + c


def with_currying(a):
    def inner_1(b):
        def inner_2(c):
            return a + b + c
        return inner_2
    return inner_1


sum_five = with_currying(5)
sum_five_and_six = with_currying(5)(6)


# complex function: a complex operation
# using currying and closure to define a structure of function
def closure_currying_function(x):
    groups_num = 3

    def inner_anonimous_function(y):
        return x(list(map(lambda i: i % groups_num, y)))
    return inner_anonimous_function


# partial function
def validate_number_member(x, y): return x[1] >= y


minimum_3_members = partial(validate_number_member, y=4)


# normal function to generate data
def counting_member_groups(list_member):
    return dict(Counter(list_member))


def which_group_has_more_members(x):
    def inner_methods_1(y):
        def inner_methods_2(z):
            return list(map(x, list(filter(y, list(z.items())))))
        return inner_methods_2
    return inner_methods_1


group_members = closure_currying_function(counting_member_groups)([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
which_group_has_more_members(print)(minimum_3_members)(group_members)

# curiosing sing
def a(x):
    print("a")
    def b(y):
        print("b")
        return x(y)
    return b


def d(x):
    print("d")
    def c(y):
        print("c")
        return x + y
    return c


print(a(d)(5)(4))


'''

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

# currying
print("using currying")
print(with_currying(5)(6)(7))
print(without_currying(5, 6, 7))
print(sum_five(6)(7))
print(sum_five_and_six(7))
'''

