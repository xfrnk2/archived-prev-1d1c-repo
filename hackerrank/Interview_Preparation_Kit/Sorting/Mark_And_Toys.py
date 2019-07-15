# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting
def maximumToys(prices, k):
    if prices == [] or k == 0:
        return 0
    prices.sort()
    value = 0
    count = 0
    for x in prices:
        if k < value + x:
            break
        value, count = value + x, count + 1

    return count
