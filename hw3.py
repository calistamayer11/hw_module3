def find_pairs_naive(first, target):
    answers = set()
    for i in range(len(first) - 1):
        for j in range(i + 1, len(first)):
            if first[i] + first[j] == target:
                answers.add((first[i], first[j]))
    return answers


def find_pairs_optimized(list_of_pairs, target):
    integers_pair_dict = {}
    answers = set()
    for index, value in enumerate(list_of_pairs):
        # check if one of the answers is in the dictionary. unsure which number to check, but if the answer is in the dictionary, shouldn't duplicate.
        if target - value in list_of_pairs:

            item_index = list_of_pairs.index(target - value)

            if not item_index in integers_pair_dict:
                # integers_pair_dict[item_index] = target - value
                integers_pair_dict[index] = value
                answers.add(target - value, value)
    return answers


def measure_min_time():
    pass


target = 7
integer_list = [1, 2, 3, 4, 5]
print(find_pairs_naive(integer_list, target))
