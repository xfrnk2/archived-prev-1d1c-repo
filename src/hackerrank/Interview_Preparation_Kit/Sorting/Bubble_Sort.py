def countSwaps(a):
    length = len(a)
    count, first_value, last_value = 0, 0, 0

    if length < 2:
        pass
    else:
        for i in range(length):
            for j in range(length - 1):
                if a[j] > a[j + 1]:
                    a[j], a[j + 1] = a[j + 1], a[j]
                    count += 1

        first_value, last_value = a[0], a[-1]

        print(f"Array is sorted in {count} swaps.")
        print(f"First Element: {first_value}")
        print(f"Last Element: {last_value}")

    return count, first_value, last_value