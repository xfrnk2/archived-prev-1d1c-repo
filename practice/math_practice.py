def gcd_function(a, b):
    while b > 0:
        a, b = b, a%b
    return a
print(gcd_function(48, 9))


from math import gcd

# 최대공약수
print(gcd(48, 9))
# 최소공배수(두수의 곱 // 최소공배수)
print(48 * 9 // gcd(48, 9))