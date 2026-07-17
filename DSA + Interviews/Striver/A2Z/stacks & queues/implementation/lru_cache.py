class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # Maps key -> Node
        
        # Initialize dummy head and tail to avoid edge cases with null pointers
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node(self, node: Node) -> None:
        """
        Helper: Insert a new node right after the dummy head 
        (representing the most recently used position).
        """
        temp = self.head.next
        
        node.next = temp
        node.prev = self.head
        self.head.next = node
        
        temp.prev = node

    def _remove_node(self, node: Node) -> None:
        """
        Helper: Unlink/delete an existing node from the doubly linked list.
        """
        prev_node = node.prev
        next_node = node.next
        
        node.prev = None
        node.next = None
        
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        """
        Return the value of the key if it exists, otherwise return -1.
        Don't forget to mark it as most recently used.
        """
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove_node(node)
        self._add_node(node)
        
        return node.val

    def put(self, key: int, value: int) -> None:
        """
        Update the key-value pair if it exists, or insert it if it doesn't.
        If capacity is exceeded, evict the least recently used node (at the tail).
        """
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self._remove_node(node)
            self._add_node(node)
        else:
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_node(new_node)
    
            if len(self.cache) > self.capacity:
                lru = self.tail.prev
                self._remove_node(lru)
                del self.cache[lru.key]
