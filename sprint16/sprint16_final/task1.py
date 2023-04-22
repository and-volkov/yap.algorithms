from typing import List, Union


class DeqError(Exception):
    def __init__(self, message="error"):
        self.message = message
        super().__init__(self.message)


class DequeSized:
    def __init__(self, max_size: int):
        self.dequeue: List[Union[int, None]] = [None] * max_size
        self.max_size: int = max_size
        self.head: int = 0
        self.tail: int = 0
        self.size: int = 0

    def _is_empty(self) -> bool:
        if self.size != 0:
            return False
        else:
            raise DeqError

    def _is_not_max_sized(self) -> bool:
        if self.size != self.max_size:
            return True
        else:
            raise DeqError

    def push_front(self, x: Union[int, None]) -> None:
        if self._is_not_max_sized():
            self.dequeue[(self.head - 1) % self.max_size] = x
            self.head = self.head - 1
            self.size += 1

    def push_back(self, x: Union[int, None]) -> None:
        if self._is_not_max_sized():
            self.dequeue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_size
            self.size += 1

    def pop_front(self) -> Union[int, str, None]:
        if not self._is_empty():
            value = self.dequeue[self.head]
            self.dequeue[self.head] = None
            self.head = (self.head + 1) % self.max_size
            self.size -= 1
            return value

    def pop_back(self) -> Union[int, str, None]:
        if not self._is_empty():
            value = self.dequeue[self.tail - 1]
            self.dequeue[self.tail - 1] = None
            self.tail = (self.tail - 1) % self.max_size
            self.size -= 1
            return value


if __name__ == "__main__":
    commands_count = int(input())
    deq_size = int(input())
    deq = DequeSized(deq_size)
    for _ in range(commands_count):
        command = input().split()
        call = getattr(deq, command[0])
        try:
            try:
                call(command[1])
            except IndexError:
                print(call())
        except DeqError as e:
            print(e)
