from stack import Stack


def is_balanced(input_str):
    stk = Stack()
    for char in input_str:
        if char == "(":
            stk.push(char)
        if char == ")":
            if stk.size() == 0:
                return False
            stk.pop()
    return stk.size() == 0


