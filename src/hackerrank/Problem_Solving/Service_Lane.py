import sys
def serviceLane(n, cases, width):
    result = []

    for case in cases:

        low, high = min(case), max(case)
        minimum_value = sys.maxsize

        for value in width[low:high + 1]:
            minimum_value = min(value, minimum_value)

        result.append(minimum_value)

    return result