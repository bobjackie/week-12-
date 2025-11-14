# Objective:
# Students will understand how to create, modify, and access elements in Python lists.

# Topics Covered:
# Creating lists, indexing, slicing, appending, popping, sorting, reversing.

# Examples:

my_list = ['apple', 'banana', 'cherry']
print(my_list[0])         # apple
print(my_list[1:])        # ['banana', 'cherry']

my_list.append('grape')
print(my_list)

my_list.pop(1)
print(my_list)

numbers = [3, 1, 4, 2]
numbers.sort()
print(numbers)
print(type(numbers))
print(numbers[0])
print(numbers[1:4]) 
print(numbers[0:])   

numbers.append(6)
print(numbers)
numbers.extend([10,11,12,13,14,15])
print(numbers)
numbers.extend(list(range(15, 550)))
print(numbers)
numbers.extend(list(range(550, 1000)))
print(numbers)

new_list =['a','b','c']
print(new_list)
new_list.append('d')
print(new_list)
removed_item = new_list.pop()
print(removed_item)
print(new_list)
remove_second_item = new_list.pop(1)
print(remove_second_item)
print(new_list)

number = [4, 2, 5, 1, 3]
number.sort()
print(number)

number.reverse()
print(number)
number.insert(2, 10)
print(number)
third_list = [7, 8, 9]
third_list[0] = 6
print(third_list)
third_list[-1] = 10
print(third_list)


import random
random_list = random.sample(range(1, 100), 10)
print(random_list) 
print(sorted(random_list))


sorted_list = sorted(random_list)
print(sorted_list)


# Practice Problems:

# Create a list with 5 of your favorite foods.
my_list1 = ['vegtable','whole grain bread','gingerbread chai','vegimite','chick-fila']
print(my_list1)


# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.