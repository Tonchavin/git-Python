import random

my_list = [random.randint(0, 10) for i in range(20)]
print(my_list)

count_dict = {}

for item in my_list:
    count_dict[item] = count_dict.get(item, 0) + 1

print(count_dict)