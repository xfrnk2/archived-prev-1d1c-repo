class Calculator:
    def __init__(self):
        self.__stack = []

    def is_stack_full(self):
        return 8 <= len(self.__stack)

c = Calculator()
print(c.is_stack_full())