class DLLNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        return "DLLNode object: data={}".format(self.data)

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

    def get_previous(self):
        """Return the self.previous attribute"""
        return self.previous

    def set_previous(self, new_previous):
        """Replace the existing value of self.previous attribute with new_previous parameter"""
        self.previous = new_previous



class DLL:

    def __init__(self):
        self.head = None

    def __repr__(self):
        return "<DLL Object: head=>".format(self.head)

    def is_empty(self):
        return self.head is None

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
        while current is not None:  # While there are still nodes left to count
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

    def add_front(self, data):
        """Add a node whose data is the new_data argument to the front of the Linked List"""
        temp = DLLNode(new_data)
        temp.set_next(self.head)

        if self.head is not None:
            self.head.set_pervious(temp)
        self.head = temp

    def remove(self, data):
        """
        The time complexity is O(n) because in worst case we have to visit every node to remove the last node.
        """
        if self.head is None:
            return "Linked list is empty, no Nodes to remove"

        current = self.head
        found = False

        while not found:
            if current.get_data() == data:
                found = True
            else:
                if current.get_next() is None:
                    return "A node with that data value is not present."
                else:
                    current = current.get_next()

        if current.previous is None:
            self.head = current.get_next()
        else:
            current.previous.set_next(current.get_next())
            current.next.set_previous(current.get_previous())



#programming foundation: object-oriented design
#python essential training
