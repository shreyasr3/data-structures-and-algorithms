class SLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "SLLNode object: data={}".format(self.data)

    def get_data(self):
        """Return the self.data attribute"""
        return self.data

    def set_data(self, new_data):
        """Replace the existing value of self.data attribute with new_data parameter"""
        self.data = new_data

    def get_next(self):
        """Return the self.next attribute"""
        return self.next

    def set_next(self, new_next):
        """Replace the existing value of self.next attribute with new_next parameter"""
        self.next = new_next


class SLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "SLL Object: head={}".format(self.head)

    def is_empty(self):
        """Returns True if the linked list is empty, else False"""
        return self.head is None   # self.head == 1

    def add_front(self, new_data):
        """Add a node whose data is the new_data argument to the front of the Linked List"""
        temp = SLLNode(new_data)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """Traverses the Linked List and returns an integer values representing the
        number of nodes in the Linked List.

        The time complexity is O(n) because every node in the Linked list must be visited
        in order to calculate the size of the Linked List.
        """
        size = 0
        if self.head is None:
            return 0

        current = self.head
        while current is not None:   #While there are still nodes left to count
            size += 1
            current = current.get_next()

        return size

    def search(self, data):
        """Traverses the linked list and it returns true if the data searched for
        is present in one of the nodes.

        The time complexity is O(n) because in worst case we have to go through all nodes.
        """
        if self.head is None:
            return "Linked list is empty. No nodes to search."

        current = self.head
        while current is not None:
            # the Node's data matches what we are looking for
            if current.get_data() == data:
                return True
            # The node doesn't match
            else:
                current = current.get_next()

        return False

    def remove(self, data):
        """Removes the first occurence of a Node that contains the data argument

        The time complexity is O(n) because in the worst case we have to traverse through to the last node.
        """
        if self.head is None:
            return "Linked List is empty, no Nodes to remove."

        current = self.head
        previous = None
        found = False

        while not Found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() == None:
                    return "A node with that data value is not present."
                else:
                    previous = current
                    current = current.get_next()

        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())


