data = open('input_day8.txt', 'r').read().split('\n')
tree_score = list()

for r_in, line in enumerate(data):
    for c_in, tree in enumerate(line):
        left_score = 0
        right_score = 0
        top_score = 0
        bot_score = 0
        size = int(tree)

        for left_tree in reversed(list(line[:c_in])):
            if int(left_tree) < size:
                left_score += 1
            else:
                left_score += 1
                break

        for right_tree in line[c_in+1:]:
            if int(right_tree) < size:
                right_score += 1
            else:
                right_score += 1
                break

        top = list()
        bottom = list()
        for index, line2 in enumerate(data):
            if index < r_in:
                top.append(int(line2[c_in]))
            elif index > r_in:
                bottom.append(int(line2[c_in]))

        for bot_trees in bottom:
            if int(bot_trees) < size:
                bot_score += 1
            else:
                bot_score += 1
                break

        for top_trees in reversed(top):
            if int(top_trees) < size:
                top_score += 1
            else:
                top_score += 1
                break

        tree_score.append(left_score * right_score * bot_score * top_score)

print(max(tree_score))
