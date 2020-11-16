# Which line of code will change start_dic to the final_dic
starting_dictionary = {
    "a": 9,
    "b": 8,
}

# final_dictionary = starting_dictionary.append({"c":7})

# final_dictionary = starting_dictionary += {"c":7}

# final_dictionary = starting_dictionary["c"] : 7


starting_dictionary["c"] = 7
final_dictionary =  starting_dictionary

print(final_dictionary)

# Which line of code will produce an error?
dict = {
    "a":1,
    "b":2,
    "c":3,
}

# dict["c"] = [1,2,3]

# for key in dict:
#   dict["c"] += 1

# dict[1] =4


#--------Error --------
# print(dict[1])
#--------Error ---------

order = {
    "starter": {1: "Salad", 2: "Soup"},
    "main": {1:["Burger", "Fries"], 2:["Steak"]},
    "dessert": {1: ["Ice Cream"], 2: []}
}

# print(order["main"][2])

# print(order["desert" -1][2][0])

# print(order[main][2][0])

print(order["main"][2][0])











