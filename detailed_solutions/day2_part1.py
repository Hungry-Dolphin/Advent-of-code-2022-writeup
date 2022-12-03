result = {
    "A X": 4,
    "A Y": 8,
    "A Z": 3,
    "B X": 1,
    "B Y": 5,
    "B Z": 9,
    "C X": 7,
    "C Y": 2,
    "C Z": 6,
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

print(score_counter)
