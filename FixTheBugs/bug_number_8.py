#Max Holdaway Find the Bug number 8

def add_to_list(item, my_list=[]):

     my_list.append(item)

     return my_list

ItemToBeAdded1 = "Hello"

ItemToBeAdded2 = 1

print(f"{add_to_list(ItemToBeAdded1)}")