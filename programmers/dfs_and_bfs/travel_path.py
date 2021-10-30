from bisect import bisect_left, bisect_right


def solution(tickets):
    tickets.sort(key=lambda x: (x[0], x[1]))
    keys = [t[0] for t in tickets]
    visits = set()
    results = []
    # idx = keys.index('ICN')

    result = []

    def func(curr):
        nonlocal result, visits

        for idx in range(bisect_left(keys, curr), bisect_right(keys, curr)):
            c, des = tickets[idx]
            print(c, des, result)

            if (c, des) in visits:
                continue

            visits.add((c, des))
            result.append(curr)

            func(des)

        if len(result) == len(tickets):
            result.append(curr)
        print(result)

        result = []

    func('ICN')





