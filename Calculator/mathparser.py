import math_functions as mf


def parse_to_postfix_annotation(exp: str) -> str:
    postfix_result = ""
    exp = exp.replace(' ', '')
    exp_len = len(exp)
    stack = []
    priorities = {'(': 0, ')': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3, '~': 4}
    j = 0
    while j < exp_len:
        i = exp[j]
        if i == '-' and (j == 0 or (j > 1 and not exp[j-1].isdigit())):
            i = '~'
        if i.isdigit():
            while j < exp_len and (exp[j].isdigit() or exp[j] == '.'):
                postfix_result += exp[j]
                j += 1
            j -= 1
            postfix_result += ' '
        elif i == '(':
            stack.append(i)
        elif i == ')':
            if stack.count('(') == 0:
                raise Exception("Problem with parenthesis")
            while stack[-1] != '(':
                postfix_result += stack[-1] + ' '
                stack.pop(-1)
            stack.pop(-1)

        elif len(stack) > 0 and priorities[i] <= priorities[stack[-1]]:
            while len(stack) and priorities[i] <= priorities[stack[-1]]:
                postfix_result += stack[-1] + ' '
                stack.pop(-1)
            stack.append(i)
        else:
            stack.append(i)
        j += 1
    while len(stack):
        postfix_result += stack[-1] + ' '
        stack.pop(-1)
    return postfix_result


def parse_postfix_to_float(postfix_expression: str) -> float:
    x = 0
    y = 0
    postfix_expression = postfix_expression.split()
    stack = []
    for i in postfix_expression:
        if len(i) > 1 or i.isdigit():
            stack.append(float(i))
        elif i == '~':
            if len(stack) == 0:
                raise Exception("Problem with expression")
            stack[-1] = -stack[-1]
        else:
            if len(stack) < 2:
                raise Exception("Problem with expression")
            x = stack[-2]
            y = stack[-1]
            stack.pop(-1)
            stack[-1] = mf.dict_with_functions[i](x, y)
    if len(stack) > 1:
        raise Exception("Problem with expression")
    return stack[0]



