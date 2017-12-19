"""Linked list."""


class LinkedList(object):
    """Class for a linked list."""

    def __init__(self, iterable=None):
        """On list creation set head to none."""
        self.head = None
        self.length = 0
        if isinstance(iterable, (str, tuple, list)):
            for i in iterable:
                self.push(i)

    def push(self, val):
        """Push a val to the list."""
        self.head = Node(val, self.head)
        self.length += 1

    def pop(self):
        """Remove the head of the list and return it."""
        if self.head is None:
            return "List is empty, cannot pop from an empty list"
        val = self.head
        self.head = self.head.next_node
        self.length -= 1
        return val

    def search(self, val):
        """Search list for given value and return the node."""
        current = self.head
        while current:
            if current.val == val:
                return current
            current = current.next_node

    def remove(self, node):
        """Remove a node from the linked list."""
        current = self.head
        node_to_remove = None
        while current:
            if current.next_node == node:
                node_to_remove = current.next_node
                self.length -= 1
                current.next_node = current.next_node.next_node
            current = current.next_node

        if node_to_remove is None:
            return "Node was not found in list"

    def size(self):
        """Return the length of the list."""
        return self.length

    def display(self):
        """Display the list."""
        return self.__str__()

    def __len__(self):
        """Redifine the built in len function for the list."""
        return self.length

    def __str__(self):
        """Return a tuple list."""
        thing = '('
        thing += str(self.head.val)
        current_node = self.head
        while current_node.next_node:
            thing += ', ' + str(current_node.next_node.val)
            current_node = current_node.next_node
        thing += ')'
        return thing


class Node(object):
    """Class for node."""

    def __init__(self, val, next_node=None, prev_node=None, priority=0):
        """Create a new node."""
        self.val = val
        self.next_node = next_node
        self.prev_node = prev_node
        self.priority = priority


def addTwoLists(first, second):  # pragma: no cover
    if not first.head and second.head:
        raise ValueError('one of your lists is empty')
    first, second = first.head, second.head
    prev = None
    temp = None
    hold = 0

    while(first or second):
        if not first:
            firstval = 0
        else:
            firstval = first.val
        if not second:
            secondval = 0
        else:
            secondval = second.val
        sumof = hold + firstval + secondval

        if sumof >= 10:
            hold = 1
        else:
            hold = 0

        if sumof < 10:
            sumof = sumof
        else:
            sumof = sumof % 10

        temp = Node(sumof)
        res_ll = LinkedList()

        if res_ll.head is None:
            res_ll.head = temp
        else:
            prev.next_node = temp

        prev = temp

        if first is not None:
            first = first.next_node
        if second is not None:
            second = second.next_node

    if hold > 0:
        temp.next_node = Node(hold)
    return res_ll
