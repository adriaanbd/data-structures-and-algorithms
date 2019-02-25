def get_brackets(string: str) -> list:
    open_br = '(', '[', '{'
    close_br = ')', ']', '}'
    brackets = list()
    for char in string:
        if char in open_br or char in close_br:
            brackets.append(char) 
    return brackets


def balanced_brackets(string: str) -> bool:
    open_br = '(', '[', '{'
    close_br = ')', ']', '}'
    stack = list()
    for bracket in get_brackets(string):
        if bracket in open_br:
            stack.append(bracket)
        elif len(stack) == 0:
            return False 
        else:
            top = stack.pop()
            if top == open_br[0] and bracket != close_br[0]:
                return False
            elif top == open_br[1] and bracket != close_br[1]:
                return False
            elif top == open_br[2] and bracket != close_br[2]:
                return False
    if len(stack) == 0: 
        return True
    return False
