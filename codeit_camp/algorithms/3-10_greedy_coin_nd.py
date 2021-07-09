def min_coin_count(value, coin_list):
    cc = 0
    for coin in sorted(coin_list, reverse=True):
        m, value = divmod(value, coin)
        cc += m

    return cc


# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))