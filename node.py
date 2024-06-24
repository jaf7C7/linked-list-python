class Node:
    """A single node in a linked list data structure."""

    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, new_next):
        self._next = new_next
