def course_selection(course_list):
    course_list.sort(key=lambda x: (x[1], x[0]))

    p = 0
    t = []

    for c in course_list:
        c0, c1 = c

        if c0 > p:
            p = c1
            t.append(c)

    return t


# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
