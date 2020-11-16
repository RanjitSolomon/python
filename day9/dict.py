# Create empty directory
empty_dict = {}

# Add items
empty_dict["key"] = "An Item"
print(f"Directory contents {empty_dict}")

# update an item
empty_dict["key"] = "An updated item"
print(f"after updated item {empty_dict}")

# Delete a directory
empty_dict = {}
print(f"After deleting the contents {empty_dict}")

programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# Loop through a dictionary
# print the key
for key in programming_dictionary:
    print(key)

# print the values
for key in programming_dictionary:
    print(f"key: {key}")
    print(programming_dictionary[key])

