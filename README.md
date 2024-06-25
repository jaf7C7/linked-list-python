# Single Linked List

This is a singly linked list implemented in Python class `LinkedList`.

Nodes are added by the `LinkedList` class's `insert` method.

The python magic methods `__iter__`, `__getitem__`, `__delitem__`, and `__len__` are also implemented for convenience.

This implementation stores nodes in either ascending (the default) or descending order according the the node's `value` attribute.

To reverse the order of nodes use the instance method `reverse` to reverse the list in place.


## Example Usage

```python
>>> from linked_list import LinkedList
>>>
>>> ll = LinkedList()
>>>
>>> ll.insert(3)
>>> ll.head.value
3
>>>
>>> ll.insert(1)
>>> ll.head.value   # 1 is placed before 3 even though it was added afterwards
1
>>>
>>> ll.insert(5)
>>> ll.insert(9)
>>> for node in ll:
...     print(node.value)
...
1
3
5
9
>>> ll[1].value   # Nodes can be accessed like in a normal Python list
1
>>> del ll[1]  # Node deletion also works like in a normal list
>>> ll[1]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "D:\Courses\python-oop\linked_list\linked_list.py", line 24, in __getitem__
    raise IndexError(f'Could not find index {value}')
IndexError: Could not find index 1
>>>
>>> ll.reverse()  # Reverse the list in place, sorting nodes in descending order
>>> [n.value for n in ll]
[9, 5, 3]
>>> ll.reverse()  # Restore the ascending order
>>> [n.value for n in ll]
[3, 5, 9]
>>>
```
