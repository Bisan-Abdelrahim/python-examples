
from prime_number import prime_number
from factorial import factorial
from fibonacci import fibonacci
from class_name import class_name
from random_number import random_number
from shuffle_cards import shuffle_cards
from remove_punctuation import remove_punctuation
from sort_words import sort_words
from merge_dictionaries import merge_dictionaries
from merge_reverse_lists import merge_reverse_lists
from list_slicing import list_slicing
from remove_duplicates import remove_duplicates
from list_delete_methods import list_delete_methods
from lists_to_dictionary import lists_to_dictionary
from delete_dictionary_key import delete_dictionary_key
from flatten_list import flatten_list
from read_write_file import read_write_file
from append_file import append_file
from built_in_operators import built_in_operators
from user_input import user_input
from list_memory_address import list_memory_address


# 1. Prime Number
print("1. Prime Number:")
print(prime_number(7))

# 2. Factorial
print("\n2. Factorial:")
print(factorial(5))

# 3. Fibonacci
print("\n3. Fibonacci:")
fibonacci(7)

# 4. Class Name
print("\n\n4. Class Name:")
class Student:
    pass

student = Student()
print(class_name(student))

# 5. Random Number
print("\n5. Random Number:")
print(random_number(1, 10))

# 6. Shuffle Cards
print("\n6. Shuffle Cards:")
deck = ["A", "K", "Q", "J", "10"]
print(shuffle_cards(deck))

# 7. Remove Punctuation
print("\n7. Remove Punctuation:")
print(remove_punctuation("Hello, World!"))

# 8. Sort Words
print("\n8. Sort Words:")
print(sort_words("banana apple cherry"))

# 9. Merge Dictionaries
print("\n9. Merge Dictionaries:")
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
print(merge_dictionaries(dict1, dict2))

# 10. Merge and Reverse Lists
print("\n10. Merge and Reverse Lists:")
print(merge_reverse_lists([1, 2, 3], [4, 5, 6]))



# 11. List Slicing
from list_slicing import list_slicing

print("\n11. List Slicing:")
print(list_slicing([10, 20, 30, 40, 50], 1, 4))


# 12. Remove Duplicates
from remove_duplicates import remove_duplicates

print("\n12. Remove Duplicates:")
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))


# 13. List Delete Methods
from list_delete_methods import list_delete_methods

print("\n13. List Delete Methods:")
print("Remove:", list_delete_methods([10, 20, 30], "remove", 20))
print("Pop:", list_delete_methods([10, 20, 30], "pop", 1))
print("Del:", list_delete_methods([10, 20, 30], "del", 0))
print("Clear:", list_delete_methods([10, 20, 30], "clear"))


# 14. Convert Two Lists to Dictionary
from lists_to_dictionary import lists_to_dictionary

print("\n14. Lists to Dictionary:")
keys = ["name", "age", "city"]
values = ["Bisan", 22, "Nablus"]
print(lists_to_dictionary(keys, values))


# 15. Delete Dictionary Key

print("\n15. Delete Dictionary Key:")
student_info = {"name": "Bisan", "age": 22, "city": "Nablus"}
print(delete_dictionary_key(student_info, "age"))


# 16. Flatten Nested List

print("\n16. Flatten List:")
print(flatten_list([[1, 2], [3, 4], [5, 6]]))


# 17. Read and Write File
print("\n17. Read and Write File:")

filename = input("Enter file name: ")
content = input("Enter file content: ")

print(read_write_file(filename, content))


# 18. Append to File
print("\n18. Append to File:")

filename = input("Enter file name: ")
content = input("Enter content to append: ")

append_file(filename, content)

with open(filename, "r") as file:
    print("File content:", file.read())


# 19. Built-in Operators
print("\n19. Built-in Operators:")

numbers = list(map(int, input("Enter list numbers separated by spaces: ").split()))

coordinates = tuple(map(int, input("Enter tuple numbers separated by spaces: ").split()))

name = input("Enter student name: ")
age = int(input("Enter student age: "))

student = {"name": name, "age": age}

built_in_operators(numbers, coordinates, student)


# 20. User Input
from user_input import user_input

print("\n20. User Input:")
user_input()


# 21. List Memory Address Difference
from list_memory_address import list_memory_address

print("\n21. List Memory Address Difference:")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(list_memory_address(list1, list2))
