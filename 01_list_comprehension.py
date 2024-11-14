# List of comprehension

my_normal_list = [35, 24, 62, 52, 30, 30, 17]
my_list = [i for i in range(8)]
print(my_list)

my_range = range(10)
print(list(my_range))

def sum_five(number):
    return number + 5

my_list = [sum_five(i) for i in range(20)]
print(my_list)