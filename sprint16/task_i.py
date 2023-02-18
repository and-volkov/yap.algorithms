from typing import Any, Union


class MaxQueueSized:
    def __init__(self, max_size: int):
        self.queue = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, x: Any) -> Union[None, str]:
        if self.size != self.max_size:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print("error")

    def pop(self) -> Union[Any, None]:
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_size
        self.size -= 1
        return x

    def peek(self) -> Any:
        return self.queue[self.head]


if __name__ == "__main__":
    n = int(input())
    size = int(input())
    my_queue = MaxQueueSized(max_size=size)
    for _ in range(n):
        row = input().split(" ")
        if row[0] == "peek":
            print(my_queue.peek())
        elif row[0] == "push":
            my_queue.push(row[1])
        elif row[0] == "size":
            print(my_queue.size)
        elif row[0] == "pop":
            print(my_queue.pop())
