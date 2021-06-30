counts = dict()
data_list = [1, 2, 3, 4, 5, 6, 7, 2, 2, 3, 3, 4, 5]
for i in data_list:
    counts[i] = counts.get(i, 0) + 1
print(counts)
for i in counts.keys():
    # counts[i] = 0 # 초기화 식
    print(counts[i])