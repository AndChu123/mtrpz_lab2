class LinkedListNode:
    def __init__(self, value: str, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def length(self) -> int:
        return self._length

    def append(self, element: str) -> None:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character.")
        node = LinkedListNode(element)
        if not self.head:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        self._length += 1

    def insert(self, element: str, index: int) -> None:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character.")
        if index < 0 or index > self._length:
            raise IndexError("Index out of range.")
        node = LinkedListNode(element)
        if index == 0:
            node.next = self.head
            if self.head:
                self.head.prev = node
            self.head = node
            if self._length == 0:
                self.tail = node
        elif index == self._length:
            self.append(element)
            return
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            node.prev = curr.prev
            node.next = curr
            curr.prev.next = node
            curr.prev = node
        self._length += 1

    def delete(self, index: int) -> str:
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range.")
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
        elif index == self._length - 1:
            value = self.tail.value
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
        else:
            curr = self.head
            for _ in range(index):
                curr = curr.next
            value = curr.value
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        self._length -= 1
        return value

    def deleteAll(self, element: str) -> None:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character.")
        curr = self.head
        while curr:
            next_node = curr.next
            if curr.value == element:
                if curr.prev:
                    curr.prev.next = curr.next
                else:
                    self.head = curr.next
                if curr.next:
                    curr.next.prev = curr.prev
                else:
                    self.tail = curr.prev
                self._length -= 1
            curr = next_node

    def get(self, index: int) -> str:
        if index < 0 or index >= self._length:
            raise IndexError("Index out of range.")
        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.value

    def clone(self):
        new_list = LinkedList()
        curr = self.head
        while curr:
            new_list.append(curr.value)
            curr = curr.next
        return new_list

    def reverse(self) -> None:
        curr = self.head
        self.head, self.tail = self.tail, self.head
        while curr:
            curr.prev, curr.next = curr.next, curr.prev
            curr = curr.prev

    def findFirst(self, element: str) -> int:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character.")
        curr = self.head
        idx = 0
        while curr:
            if curr.value == element:
                return idx
            curr = curr.next
            idx += 1
        return -1

    def findLast(self, element: str) -> int:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character.")
        curr = self.tail
        idx = self._length - 1
        while curr:
            if curr.value == element:
                return idx
            curr = curr.prev
            idx -= 1
        return -1

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self._length = 0

    def extend(self, elements) -> None:
        if not isinstance(elements, LinkedList):
            raise ValueError("Argument must be a LinkedList.")
        curr = elements.head
        while curr:
            self.append(curr.value)
            curr = curr.next 