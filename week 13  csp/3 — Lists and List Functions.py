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

# Practice Problems:

# Create a list with 5 of your favorite foods.
my_list1 = ['vegtable','whole grain bread','gingerbread chai','vegimite','chick-fila']
print(my_list1)


# Print the second and last item.

# Add a new item using .append().

# Remove the first item using .pop(0).

# Reverse your list using .reverse().

# Create a list of 3 lists (matrix), and access the middle element.