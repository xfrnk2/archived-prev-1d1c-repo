import string

def func(s, n):

    alpha_dic = {alphabet : i for i, alphabet in enumerate(string.ascii_lowercase)}
    size = len(alpha_dic)
    key_array = []

    for x in s:
        if x.isalpha():
            condition = False

            if x.isupper():
                x = x.lower()
                condition = True

            num = alpha_dic[x] + n

            if size <= num:
                num %= size

            key_array.append((num, condition))

    alpha_dic = {i : alphabet for alphabet, i in alpha_dic.items()}
    result = ""

    for x in s:
        if x.isalpha():
            num, condition = key_array.pop(0)
            value = alpha_dic[num]

            if condition:
                value = value.upper()

            result+=value
        else:
            result+=" "

    return result


print(func("AB", 1))
print(func("z", 1))
print(func("a B z", 4))