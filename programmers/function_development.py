def solution(progresses, speeds):
    answer = []
    data_length = len(progresses)
    location = 0

    while data_length > location:

        for i in range(data_length):
            progresses[i] += speeds[i]

        if progresses[location] >= 100:
            movement_count = 0

            for j in range(location, data_length):
                if 100 <= progresses[j]:
                    movement_count += 1
                else:
                    break
            answer.append(movement_count)
            location += movement_count

    return answer