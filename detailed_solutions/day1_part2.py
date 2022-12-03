import heapq

# We know that our input will be a list of calories
# You can use this file by using the open() function in 'r' (read) mode
elf_rations_text = open('input_day1.txt', 'r').read()

# Since we know each elf is denoted by a empty line we can seperate this list
# We use this by using .split() every time we see a double newline (\n)
elf_rations_list = elf_rations_text.split('\n\n')
# We now have a list of all elves and the snacks they carry

# We create a list of our own to keep track of the calories per elf
calorie_list = []

# For each elf that is on this list
for elf_ration_text in elf_rations_list:
    # We need to get a list of their snacks
    # This can be done by seperating the snacks by single newline (\n)
    snack_list = elf_ration_text.split("\n")

    # We now need to keep track of the amount of calories this elf caries
    calories = 0

    # For snack that this elf carries add the calories to our counter
    for snack in snack_list:
        # Our snack is still a string
        # So we need to transform it to an interger by using int()
        # Then we can add the calories of this snack by using +=
        calories += int(snack)

    # We now know how much calories this elf carries, we add it to our list
    calorie_list.append(calories)

# We inport the heapq module to automatically fetch the 3 biggest values
top_3 = heapq.nlargest(3, calorie_list)

# We need to add all values in this list together to get our answer
answer = 0

for item in top_3:
    # We do the same thing that we did before in the snack list
    answer += int(item)

print(answer)
