class ArrayList:
    def __init__(self):
        self._data = []

    def length(self) -> int:
        return len(self._data)

    def append(self, element: str) -> None:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character.")
        self._data.append(element)

    def insert(self, element: str, index: int) -> None:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character.")
        if index < 0 or index > len(self._data):
            raise IndexError("Index out of range.")
        self._data.insert(index, element)

    def delete(self, index: int) -> str:
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of range.")
        return self._data.pop(index)

    def deleteAll(self, element: str) -> None:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character.")
        self._data = [x for x in self._data if x != element]

    def get(self, index: int) -> str:
        if index < 0 or index >= len(self._data):
            raise IndexError("Index out of range.")
        return self._data[index]

    def clone(self):
        new_list = ArrayList()
        new_list._data = self._data.copy()
        return new_list

    def reverse(self) -> None:
        self._data.reverse()

    def findFirst(self, element: str) -> int:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character.")
        try:
            return self._data.index(element)
        except ValueError:
            return -1

    def findLast(self, element: str) -> int:
        if not isinstance(element, str) or len(element) != 1:
            raise ValueError("Element must be a single character.")
        for i in range(len(self._data) - 1, -1, -1):
            if self._data[i] == element:
                return i
        return -1

    def clear(self) -> None:
        self._data.clear()

    def extend(self, elements) -> None:
        if not isinstance(elements, ArrayList):
            raise ValueError("Argument must be an ArrayList.")
        self._data.extend(elements._data.copy()) 