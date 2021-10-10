class Deque:
    class Node:
        def __init__(self, data):
            self.data = data
            self.prev = None
            self.next = None

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_left(self, data):
        new_node = self.Node(data)
        new_node.prev = None

        if self.head is None:
            new_node.next = None
            self.head = new_node
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_right (self, data):
        new_node = self.Node(data)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop_left(self):
        prev_head = self.head
        if self.head is None:
            return
        if prev_head.next is not None:
            prev_head.next.prev = None
        else:
            self.tail = None
        self.head = prev_head.next
        return prev_head.data

    def pop_right(self):
        prev_tail = self.tail
        if self.tail is None:
            return
        if prev_tail.prev is not None:
            prev_tail.prev.next = None
        else:
            self.head = None
        self.tail = prev_tail.prev
        return prev_tail.data

    def deque_to_list(self):
        output = list()
        curr = self.head
        while curr is not None:
            output.append(curr.data)
            curr = curr.next
        return output

    def search_by_id(self, id):
        curr = self.head
        index = 0
        while index < id and curr is not None:
            curr = curr.next
            index += 1
        if curr is None:
            return
        return curr.data

    def get_left(self):
        if self.head is None:
            print("Deque is Empty")
        else:
            return self.head.data

    def get_right(self):
        if self.head is None:
            print("Deque is Empty")
        else:
            return self.tail.data

if __name__ == '__main__':
    dq = Deque()
    dq.insert_left(0)
    dq.insert_right(33)
    dq.insert_right(5)
    dq.insert_left(10)
    dq.insert_right(23)
    print (dq.deque_to_list())
    print (dq.pop_left())
    print (dq.deque_to_list())
    print (dq.search_by_id(1))