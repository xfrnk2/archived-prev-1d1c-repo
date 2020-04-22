def get_result(sentence: str) -> bool:
    bracket_stack = []

    for s in sentence:

        if s.isalpha():
            continue

        elif s == "(":
            bracket_stack.append(1)

        elif s == "[":
            bracket_stack.append(0)

        elif s == ")" or s == "]":

            try:
                if bracket_stack[-1] == 0 and s == ")":
                    return False
                elif bracket_stack[-1] == 1 and s == "]":
                    return False
                bracket_stack.pop()

            except IndexError:
                return False

    if bracket_stack:
        return True
        #if stack is empty, return True


if __name__ == '__main__':
    sentence_list = []

    while True:
        get_input = input()
        if get_input == '.':
            break
        sentence_list.append(get_input)

    for x in sentence_list:
        if get_result(x):
            print('yes')
        else:
            print('no')