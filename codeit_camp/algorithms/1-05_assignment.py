def is_palindrome(word):
    pivot = len(word) // 2

    for i in range(1, pivot + 1):
        if word[pivot - i] != word[pivot + i]:
            return False

    return True

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))