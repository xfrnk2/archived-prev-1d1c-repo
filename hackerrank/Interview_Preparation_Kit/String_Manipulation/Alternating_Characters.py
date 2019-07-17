def alternatingCharacters(s):
    count = 0
    if s == "" or type(s) is not str:
        return count
    front_value = None
    for x in s:
        if x == front_value:
            count += 1
        front_value = x
    return count