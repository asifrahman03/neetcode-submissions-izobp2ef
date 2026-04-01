class Node:
    def __init__(self, key, val, prev, next):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curr_size = 0
        self.cache = {}
        self.head = Node(None, None, None, None)
        self.tail = Node(None, None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        got_node = self.cache[key]
        got_node.prev.next = got_node.next
        got_node.next.prev = got_node.prev
        
        prev_end = self.tail.prev
        self.tail.prev = got_node
        got_node.next = self.tail
        got_node.prev = prev_end
        prev_end.next = got_node
        return got_node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            # Shift to MRU
            got_node = self.cache[key]
            got_node.prev.next = got_node.next
            got_node.next.prev = got_node.prev
            
            prev_end = self.tail.prev
            self.tail.prev = got_node
            got_node.next = self.tail
            got_node.prev = prev_end
            prev_end.next = got_node
            return

        new_node = Node(key, value, None, None)
        if self.curr_size == self.capacity:
            got_node = self.head.next
            got_node.prev.next = got_node.next
            got_node.next.prev = got_node.prev
            self.curr_size -= 1
            del self.cache[got_node.key]
        prev_end = self.tail.prev
        self.tail.prev = new_node
        new_node.next = self.tail
        new_node.prev = prev_end
        prev_end.next = new_node
        self.curr_size += 1
        self.cache[key] = new_node
        
