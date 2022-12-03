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

note = open('input_day2.txt', 'r').read().split('\n')
print(sum([result[line] for line in note]))
