#!/usr/bin/env python3


class DLNode:

    def __init__(self, value, backward, forward):
        self.value = value
        self.backward = backward
        self.forward = forward

    def __repr__(self):
        return f'[{self.value}]'

    def is_reactable(self):
        if self.backward:
            prev = self.backward.value
            curr = self.value
            return (prev != curr and prev.lower() == curr.lower())
        return False



class DLIterator:

    def __init__(self, dl):
        self.pointer = dl.root

    def __next__(self):
        if self.pointer is None:
            raise StopIteration
        else:
            current = self.pointer
            self.pointer = self.pointer.forward
            return current


class DL:

    def __init__(self, seq=None):
        self.root = None
        self.head = None
        self.length = 0
        if seq:
            for item in seq:
                self.append(item)

    def __len__(self):
        return self.length

    def append(self, value):
        n = DLNode(value, None, None)
        if self.root is None:
            self.root = n
            self.head = n
            self.length = 1
        else:
            self.head.forward = n
            n.backward = self.head
            self.head = n
            self.length += 1
        return n

    def __iter__(self):
        return DLIterator(self)

    def __str__(self):
        return ''.join([
            str(n.value) for n in self
            ])

    def react(self, node):
        if not node.is_reactable():
            return 0
        if self.length == 2:
            self.root.forward = None
            self.head.backward = None
            self.root = self.head = None
            self.length = 0
            return 1
        curr = node
        prev = node.backward
        if prev.backward is None:  # at begin of list
            self.root = curr.forward
            curr.forward.backward = None
        elif curr.forward is None:  # As end of list
            self.head = prev.backward
            prev.backward.forward = None
        else:  # in the middle
            prev.backward.forward = curr.forward
            curr.forward.backward = prev.backward
        curr.forward = None
        curr.backward =  None
        prev.forward = None
        prev.backward = None
        del curr
        del prev
        self.length -= 2
        return 1

    def reduce(self):
        num_changes = -1
        while num_changes != 0:
            num_changes = 0
            for n in self:
                num_changes += self.react(n)
