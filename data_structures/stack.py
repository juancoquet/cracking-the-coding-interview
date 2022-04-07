class Stack:

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)



# Take a space-separated infix expression and convert it to a postfix expression

def infix_to_postfix(infix_expr):
    op_precedence = {
        '*': 3,
        '/': 3,
        '+': 2,
        '-': 2,
        '(': 1,
    }
    operators = Stack()
    postfix = []
    tokens = infix_expr.split(' ')

    for token in tokens:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "1234567890":
            postfix.append(token)
        elif token == "(":
            operators.push(token)
        elif token == ")":
            top_opr = operators.pop()
            while top_opr != "(":
                postfix.append(top_opr)
                top_opr = operators.pop()
        else:
            while not operators.is_empty() and \
                op_precedence[token] <= op_precedence[operators.peek()]:
                    postfix.append(operators.pop())
            operators.push(token)

    while not operators.is_empty():
        postfix.append(operators.pop())
    
    return " ".join(postfix)

print(infix_to_postfix("A * B + C * D"))


# Evaluate a space-separated postfix expression

def eval_postfix(postfix_expr):
    operands = Stack()
    tokens = postfix_expr.split(" ")

    for token in tokens:
        if token in "1234567890":
            operands.push(token)
        else:
            right_val = operands.pop()
            left_val = operands.pop()
            result = eval(str(left_val) + token + str(right_val))
            operands.push(result)
    
    return operands.pop()

print(eval_postfix("7 8 + 3 2 + /"))

            
