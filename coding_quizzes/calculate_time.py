import time
import random
from coding_quizzes.bubblesort import bubble_sort
from coding_quizzes.insertsort import insert_sort
from coding_quizzes.selectsort import sel_sort

arr = []


def rand_list():
    for _ in range(1000):
        arr.append(random.randrange(0, 10))

def Main():
    rand_list()
    for x in range(3):
        start_time = time.time()
        if x == 0:
            bubble_sort(arr)
        elif x == 1:
            insert_sort(arr)
        elif x == 2:
            sel_sort(arr)

        end_time = time.time()
        result = end_time - start_time
        print("소요시간", result)


Main()