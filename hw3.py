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
    return min(time_lst)


def print_table():
    lst_10 = [value for value in range(1, 11)]
    target_10 = 12
    lst_50 = [value for value in range(1, 51)]
    target_50 = 65
    lst_100 = [value for value in range(1, 101)]
    target_100 = 117
    lst_150 = [value for value in range(1, 151)]
    target_150 = 183
    lst_200 = [value for value in range(1, 201)]
    target_200 = 208
    lst_300 = [value for value in range(1, 301)]
    target_300 = 309
    lst_500 = [value for value in range(1, 501)]
    target_500 = 511
    list_of_tuples = [
        (10, lst_10, target_10),
        (50, lst_50, target_50),
        (100, lst_100, target_100),
        (150, lst_150, target_150),
        (200, lst_200, target_200),
        (300, lst_300, target_300),
        (500, lst_500, target_500),
    ]

    table_header = f"""n           naive             optimized\n*************************************************\n"""

    # n = ""
    # naive = ""
    # optimized = ""

    def loop_string(n, naive, optimized):
        return f"""{n}        {naive}            {optimized}\n"""

    table_footer = f"""
    -------------------------------------------------
    """

    table_string = table_header
    for n, lst, target in list_of_tuples:
        table_string += loop_string(
            n,
            measure_min_time(find_pairs_naive, lst, target),
            measure_min_time(find_pairs_optimized, lst, target),
        )
    table_string += table_footer
    return table_string


# if __name__ == '__main__':

# big_list = [value for value in range(1, 1001)]

# target = 500
# integer_list = [1, 2, 3, 4, 5]
# print(find_pairs_naive(integer_list, target))
# print(measure_min_time(find_pairs_naive, integer_list, target))
# print(find_pairs_optimized, integer_list, target)
# print(measure_min_time(find_pairs_optimized, big_list, target))
print(print_table())
