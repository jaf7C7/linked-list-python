from node import Node


class LinkedList:
    """A linked list data structure.

    Nodes are kept in order from head to tail according to the `_order` property.
    """

    def __init__(self):
        self.head = None
        self._order = 'ascending'

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __getitem__(self, value):
        for node in self:
            if node.value == value:
                return node
        raise IndexError(f'Could not find index {value}')

    def __delitem__(self, value):
        if self.head is not None and value == self.head.value:
            self.head = self.head.next
            return
        for node in self:
            if node.next.value == value:
                node.next = node.next.next
                return
        raise IndexError(f'Could not find index {value}')

    def __len__(self):
        return len(list(iter(self)))

    def _precedes(self, value, other_value):
        """Return True if other_value should precede value, else False"""
        if self._order == 'ascending':
            return other_value <= value
        elif self._order == 'descending':
            return other_value >= value

    def insert(self, value):
        """Add a node to the list.

        Create a node with the given value and insert it into the list in
        the correct position, preserving order of node values.
        """
        if self.head is None or self._precedes(self.head.value, value):
            self.head = Node(value, next=self.head)
        else:
            previous = self.head
            current = self.head.next
            while not (
                current is None
                or (
                    self._precedes(value, previous.value)
                    and self._precedes(current.value, value)
                )
            ):
                previous = previous.next
                current = current.next
            previous.next = Node(value, next=current)

    def reverse(self):
        if self._order == 'ascending':
            self._order = 'descending'
        elif self._order == 'descending':
            self._order == 'ascending'
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
