import time


def find_pairs_naive(lst, target):
    answers = set()
    for i in range(len(lst) - 1):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                answers.add((lst[i], lst[j]))
    return answers


def find_pairs_optimized(list_of_pairs, target):
    integers_pair_dict = {}
    answers = set()
    for index, value in enumerate(list_of_pairs):
        # check if one of the answers is in the dictionary. unsure which number to check, but if the answer is in the dictionary, shouldn't duplicate.
        if not target - value in integers_pair_dict:
            answers.add(target - value)
            # add current index and value to the dict
            integers_pair_dict[value] = index
            item_index = list_of_pairs.index(target - value)

            if not item_index in integers_pair_dict:
                # integers_pair_dict[item_index] = target - value
                integers_pair_dict[index] = value
                answers.add(target - value, value)
    return answers


def measure_min_time(fn, lst, target):
    elapsed_time = 0
    time_lst = []
    for i in range(10):
        start = time.time()
        find_pairs_naive(lst, target)
        end = time.time()
        elapsed_time = end - start
        elapsed_time = f"{elapsed_time:.4f}"
        time_lst.append(elapsed_time)

    # return min(time_lst)
    return time_lst


target = 7
integer_list = [1, 2, 3, 4, 5]
print(find_pairs_naive(integer_list, target))
print(measure_min_time(find_pairs_naive, integer_list, target))
print(measure_min_time(find_pairs_optimized, integer_list, target))
