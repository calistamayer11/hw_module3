import time


def find_pairs_naive(lst, target):
    """Brute force method of finding pairs"""
    answers = set()

    # scroll through first items, exclude last item
    for i in range(len(lst) - 1):
        # scroll through next item over
        for j in range(i + 1, len(lst)):
            # check for target
            if lst[i] + lst[j] == target:
                answers.add((lst[i], lst[j]))
    return answers


def find_pairs_optimized(list_of_pairs, target):
    """Use a dictionary/hashmap to cache values to find pairs"""
    integers_pair_dict = {}
    answers = set()
    for index, value in enumerate(list_of_pairs):

        other_value = target - value
        # is other value in list?
        if other_value in list_of_pairs and other_value != value:

            # check if one of the answers is in the dictionary
            if not other_value in integers_pair_dict:
                # first time around, add to set
                answers.add((value, other_value))
            # add value to hashmap
            integers_pair_dict[value] = index

    return answers


def measure_min_time(fn, lst, target):
    """Test function 10 times and return minimum run time as a formatted number string"""
    elapsed_time = 0
    time_lst = []

    for i in range(10):
        start = time.time()
        fn(lst, target)
        end = time.time()
        elapsed_time = end - start
        elapsed_time = f"{elapsed_time:.4f}"
        time_lst.append(elapsed_time)

    return min(time_lst)


def print_table():
    """Formatted table of minimum times"""
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
