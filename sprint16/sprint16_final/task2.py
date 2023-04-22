import operator
from typing import List, Union


class Stack:
    def __init__(self):
        self.stack: list = []
        self.operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.floordiv
        }

    def push(self, value: int) -> None:
        self.stack.append(value)

    def pop(self) -> Union[int, None]:
        try:
            return self.stack.pop()
        except IndexError:  # Здесь можно сразу поймать ее так?
            pass

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
            self.push(self.operations[operation](b, a))
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
