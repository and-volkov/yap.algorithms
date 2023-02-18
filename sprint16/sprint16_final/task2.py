from typing import List, Union


class Stack:
    def __init__(self):
        self.stack: list = []

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop(self) -> Union[int, None]:
        if self.stack:
            return self.stack.pop()
        else:
            return None

    def peek(self) -> Union[int, None]:
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def is_empty(self) -> bool:
        return not bool(self.stack)

    def size(self) -> int:
        return len(self.stack)

    def math_operation(self, operation: str) -> None:
        if self.size() >= 2:
            a = self.pop()
            b = self.pop()
            if operation == '+':
                self.push(a + b)
            elif operation == '-':
                self.push(b - a)
            elif operation == '*':
                self.push(a * b)
            elif operation == '/':
                self.push(b // a)
        else:
            print("error")


if __name__ == "__main__":
    my_stack = Stack()
    input_list: List[str] = input().split()
    for item in input_list:
        if item.lstrip('-').isdigit():
            my_stack.push(int(item))
        else:
            my_stack.math_operation(item)

    print(my_stack.peek())
