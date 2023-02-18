from typing import Any


class Node:
    def __init__(self, value: Any, next_item: Any = None) -> None:
        self.value = value
        self.next_item = next_item


class LinkedQueue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def put(self, x: Any) -> None:
        self.size += 1
        if not self.head:
            self.head = Node(x, None)
            self.tail = self.head
        else:
            self.tail.next_item = Node(x, None)
            self.tail = self.tail.next_item

    def get(self):
        if self.head:
            print(self.head.value)
            self.head = self.head.next_item
            self.size -= 1
        else:
            print("error")


if __name__ == "__main__":
    my_queue = LinkedQueue()
    n = int(input())
    for _ in range(n):
        row = input().split(" ")
        if row[0] == "put":
            my_queue.put(row[1])
        elif row[0] == "get":
            my_queue.get()
        elif row[0] == "size":
            print(my_queue.size)
