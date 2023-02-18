from typing import List, Union


class StackMax:
    def __init__(self):
        self.items = []
        self.current_max = []

    def push(self, item: int) -> None:
        if not self.current_max or item > self.current_max[-1]:
            self.current_max.append(item)
        else:
            self.current_max.append(self.current_max[-1])
        self.items.append(item)

    def pop(self) -> Union[int, str]:
        if self.items:
            self.current_max.pop()
            return self.items.pop()
        else:
            print("error")

    def get_max(self) -> Union[int]:

        return self.current_max[-1] if self.current_max else None


def read_input() -> List[Union[int, str]]:
    return input().split()


if __name__ == "__main__":
    stack = StackMax()
    n = int(input())
    for _ in range(n):
        row = read_input()
        if len(row) == 1:
            if row[0] == "pop":
                stack.pop()
            else:
                print(stack.get_max())
        else:
            stack.push(int(row[1]))
