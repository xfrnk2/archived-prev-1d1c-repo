def move_disk(disk_num, start_peg, end_peg):
    print("%d번 원판을 %d번 기둥에서 %d번 기둥으로 이동" % (disk_num, start_peg, end_peg))


def hanoi(num_disks, start_peg, end_peg):
    if num_disks <= 1:
        return move_disk(num_disks, start_peg, end_peg)

    mid = 6 - start_peg - end_peg
    hanoi(num_disks - 1, start_peg, mid)
    move_disk(num_disks, start_peg, end_peg)
    hanoi(num_disks - 1, mid, end_peg)

    '''
    hanoi(num_disks - 1, start_peg, end_peg - 1)
    hanoi(1, 1, end_peg)
    hanoi(num_disks - 1, 2, end_peg)
    '''
    '''
    결과적으로 3 1 3을 한다고 하면
    313 -> 212, 113, 223
    // 
    num_disks가 2개일 경우는..
    1개 2번에 갔다가
    남은 1개 3번에 가고
    2번에 간 거 3번에 간다

    1개인 경우
    목적지로 바로간다


    '''


# 테스트 코드 (포함하여 제출해주세요)
hanoi(3, 1, 3)