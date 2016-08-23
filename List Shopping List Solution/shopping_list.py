
# def read_file (d_ff): 
#     # with open(d_ff.txt) as my_file:
#     #     print my_file 
#     my_file=open ("d_ff") 
#     print my_file

# # read_file(d_ff)


def read_entire_file(my_file): 
    with open(my_file) as my_file:
        output = my_file.readlines()
        return output 
    # print output 

# def read_file_to_list(my_file):
#     with open(my_file) as my_file:
#         output_list  = my_file.readlines()
#         return output_list


# # print read_entire_file("d_ff.txt")
# # print read_entire_file("rachel_fav_foods.txt")

# list1 = read_file_to_list("d_ff.txt")
# list2 = read_file_to_list("rachel_fav_foods.txt")

# def compare(list1,list2):
#     for food in list1:
#         for thing in list2:
#             if food == thing:
#                 print "Our favorite food is the same!"
#             else:
#                 print "Our favorite food is not the same"

# compare(list1,list2)\

"""
Lists Lecture Exercise.
This project is a shopping list app.
We have a global list that will be our shopping list.
Make sure your code deals with upper and lower case.
"""
shopping_list = []


def reassign_list(list):
    shopping_list = list
    return shopping_list

def add_shopping_list(item):
    item = item.lower()
    if item not in shopping_list:
        shopping_list.append(item)
        print "%s has been added." % (item)
    else:
        print "This item %s already exists!" % (item)
    return sorted_shopping_list()


def sorted_shopping_list():
    shopping_list.sort()
    return shopping_list


def remove_item(item):
    item = item.lower()
    if item in shopping_list:
        shopping_list.remove(item)
        print "%s has been removed." % (item)
    else:
        print "%s was not on the list." % (item)
    return sorted_shopping_list()

def open_list(file_name):
    with open(file_name, mode ='a') as my_file:
        my_file.write("peaches, ice cream") 

# open_list("thingstobuy.txt")

def parse(file_name):
    read_entire_file("thingstobuy.txt")
    food1 = file_name.split(",")
    return food1 

print parse("thingstobuy.txt")
     




#     item1 = "thingstobuy.txt"[0]
# # print item1
# key1 = str(item1.split(","))
# print key1
# print item1
# food1 = key1.split(":")
# print food1
# food_list[food1[1]: float(food1[3])]  
# print food_list
# def menu_change(): 
    # # print strip_menu
    
# menu_change()

# print reassign_list(["Apple", "Orange"])
# print sorted_shopping_list()

# # TEST FUNCTIONS
# # 1 - add 4 times to your shopping list
# print add_shopping_list("apple")
# print add_shopping_list("steak")
# print add_shopping_list("beef")
# print add_shopping_list("mustard")

# # 2 - Add an item that is already in the list. what happens?
# print add_shopping_list("apple")

# # 3 - Remove an item on your list
# print remove_item("apple")

# # 4 - Remove an item that is not in the list. what happens?
# print remove_item("chicken")
