data = ['a', 'b', 'c']
l = len(data)
bool_list = [[] for _ in range(l)]

def powerset(k: int):
    if k == l:
        for x in range(k):
            if bool_list[x]:
                print(data[x], end='')
        print('\n')
    else:
        bool_list[k] = []
        powerset(k+1)
        bool_list[k] = [1]
        powerset(k+1)
powerset(0)

