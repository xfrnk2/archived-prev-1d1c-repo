def sum_in_list(search_sum, sorted_list):
    sorted_list_set = set(sorted_list)
    for element in sorted_list:
        if 15 - element in sorted_list_set:
            return True
    return False


print(sum_in_list(15, [1, 2, 5, 6, 7, 9, 11]))
print(sum_in_list(15, [1, 2, 5, 7, 9, 11]))