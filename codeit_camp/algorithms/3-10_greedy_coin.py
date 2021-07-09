def min_coin_count(value, coin_list):
    # if value % min(coin_list) != 0:
    #     return -1
    cc = 0
    coin_list.sort(reverse=True)

    i = 0
    while 0 < value:
        if coin_list[i] < value:
            cc += value // coin_list[i]
            value = value % coin_list[i]
        else:
            i += 1
    return cc


# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))