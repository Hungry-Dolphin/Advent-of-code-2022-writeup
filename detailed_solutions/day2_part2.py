result = {
    "A X": 3,
    "A Y": 4,
    "A Z": 8,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 2,
    "C Y": 6,
    "C Z": 7,
}

# This is the same operation as we did in the previous days
note = open('input_day2.txt', 'r').read().split('\n')
# We now have a list containing each line that was on the note the elf gave us

score_counter = 0

for line in note:
    # We have a dictonary of all 9 possible rounds
    # For each of those rounds we know the score that we would get
    # All we need to do is to check with which result our line matches
    score_counter += result[line]
    # We can do this using the key in a dictonary, we then gen the value back

# The only thing that differs between part 1 and 2 is the scores
# You just need to update the dictonary with the new scores
print(score_counter)
