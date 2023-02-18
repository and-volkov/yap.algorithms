from typing import List, Union


class DequeSized:
    def __init__(self, max_size: int):
        self.dequeue: List[Union[int, None]] = [None] * max_size
        self.max_size: int = max_size
        self.head: int = 0
        self.tail: int = 0
        self.size: int = 0

    def _is_empty(self) -> bool:
        return self.size == 0

    def _is_not_max_sized(self) -> bool:
        return self.size != self.max_size

    def push_front(self, x: Union[int, None]) -> None:
        if self._is_not_max_sized():
            self.dequeue[(self.head - 1) % self.max_size] = x
            self.head = self.head - 1
            self.size += 1
        else:
            print("error")

    def push_back(self, x: Union[int, None]) -> None:
        if self._is_not_max_sized():
            self.dequeue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1
        else:
            print("error")

    def pop_front(self) -> Union[int, str, None]:
        if not self._is_empty():
            value = self.dequeue[self.head]
            self.dequeue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            return value
        return "error"

    def pop_back(self) -> Union[int, str, None]:
        if not self._is_empty():
            value = self.dequeue[self.tail - 1]
            self.dequeue[self.tail - 1] = None
            self.tail = (self.tail - 1) % self.max_size
            self.size -= 1
            return value
        return "error"


if __name__ == "__main__":
    commands_count = int(input())
    deq_size = int(input())
    deq = DequeSized(deq_size)
    for _ in range(commands_count):
        command = input().split(" ")
        if command[0] == "push_front":
            deq.push_front(int(command[1]))
        elif command[0] == "push_back":
            deq.push_back(int(command[1]))
        elif command[0] == "pop_front":
            print(deq.pop_front())
        elif command[0] == "pop_back":
            print(deq.pop_back())