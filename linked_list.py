from node import Node


class LinkedList:
    """A linked list data structure.

    Nodes are kept in ascending order from head to tail according to the `<=`
    operator.
    """

    def __init__(self):
        self.head = None

    def __iter__(self):
        runner = self.head
        while runner is not None:
            yield runner
            runner = runner.next

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

    def insert(self, value):
        """Add a node to the list.

        Create a node with the given value and insert it into the list in
        the correct position, preserving ascending order of node values.
        """
        if self.head is None or value <= self.head.value:
            self.head = Node(value, next=self.head)
        else:
            previous = self.head
            runner = self.head.next
            while not (
                runner is None
                or previous.value <= value <= runner.value
            ):
                previous = previous.next
                runner = runner.next
            previous.next = Node(value, next=runner)
