from inspect import stack


def create_stack():
    stack = []
    return stack
def check_stack_empty(stack):
    if len(stack) == 0:
        return True
    else:
        return False
def push(stack, item):
    stack.append(item)
def pop(stack):
    if check_stack_empty(stack):
        return "Stack is empty"
    else:
        return stack.pop()
def peek(stack):
    if check_stack_empty(stack):
        return "Stack is empty"
    else:
        return stack[-1]

stack = create_stack()
push(stack, 1)
push(stack, 2)
p=pop(stack)
print(p)
print(stack)