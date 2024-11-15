### Funciones de orden superior ###

from functools import reduce

def sum_one(value):
    return value + 1

def sum_five(value):
    return value + 5

def sum_two_values_and_one(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)

print(sum_two_values_and_one(5, 2, sum_one))
print(sum_two_values_and_one(5, 2, sum_five))

### Closures ###

def sum_ten():
    def add(value):
        return value + 10
    return add
    
add_closures = sum_ten()
print(add_closures(10))


### Funciones de orden superior ya hechas ###

numbers = [2, 5, 10, 21, 3, 12, 15, 5, 85, 25, 6]

# Map

def multiply_two(numbers):
    return numbers * 2

print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 3, numbers)))


# Filter

def filter_values(numbers):
    if numbers > 10:
        return True
    return False

print(list(filter(filter_values, numbers)))
print(list(filter(lambda numbers: numbers > 20, numbers)))


# Reduce

def sum_three_values(one_value, two_value):
    return one_value + two_value

print(reduce(sum_three_values, numbers))