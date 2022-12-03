import string

# This is the same operation as we did in the previous days
backpacks = open('input_day3.txt', 'r').read().split('\n')
sum_of_priority = 0

for backpack in backpacks:
    # We need to split the string of this backpack in half
    # This can be done by first getting the index of the middle element
    middle_index = len(backpack)//2

    # We can now take each half of the backpack by defining a list slice
    first_half = backpack[:middle_index]
    second_half = backpack[middle_index:]
    # Slices work like this: [start:stop], no iput means everything
    # In our case we take everything untill the middle for the first half
    # And from the middle untill the end for the last half

    # To get all items which exist in both halves we can transform the halves
    # By transforming each half into a set we get all unique items
    # The & operator can be used to find all items which are in both sets
    item_type_set = set(first_half) & set(second_half)
    # This set can contain more items, but we know that the challenge said
    # That there only would be one item.
    # Thus we transform this set back to a list and take the first item
    item_type = list(item_type_set)[0]

    # We now need to get the number associated with this item type
    # luckely python has a module for this
    # Don't worry I also did not know this module existed. Found it by googling
    sum_of_priority += string.ascii_letters.index(str(item_type)) + 1
    # We add this value to our counter and add 1 since indexes start at 0
    # But our values start at 1 so thats why there is a +1

print(sum_of_priority)
