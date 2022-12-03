import string

# This is the same operation as we did in the previous days
backpacks = open('input_day3.txt', 'r').read().split('\n')
sum_of_priority = 0

# We can do the same thing that we did in the last part
# We now just need to seperate for each 3
for index_value in range(0, len(backpacks), 3):
    # Now we get a counter for each 3 elves

    # Get the 3 elves in this group by using the index
    # Remember for last part, slices work [start:end]
    # In this case we start at backpack index and end at index+3
    group = backpacks[index_value:index_value + 3]

    # We now just need to update our item type finder to use 3 values
    item_type_set = set(group[0]) & set(group[1]) & set(group[2])
    # We can get each backpack in this group by using group[backpack]

    # Same as last part
    item_type = list(item_type_set)[0]
    sum_of_priority += string.ascii_letters.index(str(item_type)) + 1

print(sum_of_priority)
