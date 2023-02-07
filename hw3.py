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
        other_value = target - value
        if other_value in list_of_pairs and other_value != value:
            if not other_value in integers_pair_dict:
                answers.add((value, other_value))
            integers_pair_dict[value] = index
    return answers


def measure_min_time(fn, lst, target):
    elapsed_time = 0
    time_lst = []
    for i in range(10):
        start = time.time()
        fn(lst, target)
        end = time.time()
        elapsed_time = end - start
        elapsed_time = f"{elapsed_time:.4f}"
        time_lst.append(elapsed_time)

    # return min(time_lst)
    return time_lst


big_list = [value for value in range(1, 1001)]

target = 500
integer_list = [1, 2, 3, 4, 5]
# print(find_pairs_naive(integer_list, target))
# print(measure_min_time(find_pairs_naive, integer_list, target))
# print(find_pairs_optimized, integer_list, target)
print(measure_min_time(find_pairs_optimized, big_list, target))
