# To implement a node in doubly linked 
# list that will store data items
class Node:
    def __init__(self, _key, _value):
        self.key = _key
        self.value = _value
        self.cnt = 1
        self.next = None
        self.prev = None


# To implement the doubly linked list
class List:
    def __init__(self):
        self.size = 0  # Size
        self.head = Node(0, 0)  # Dummy head
        self.tail = Node(0, 0)  # Dummy tail
        self.head.next = self.tail
        self.tail.prev = self.head

    # Function to add node in front
    def addFront(self, node):
        temp = self.head.next
        node.next = temp
        node.prev = self.head
        self.head.next = node
        temp.prev = node
        self.size += 1

    # Function to remove node from the list
    def removeNode(self, delnode):
        prevNode = delnode.prev
        nextNode = delnode.next
        prevNode.next = nextNode
        nextNode.prev = prevNode
        self.size -= 1


"""
- need a DLL inside a dict that keeps track of levels (dict represents frequency)
- initially
    - self.capacity to get size for resizing
    - self.minFreq to instantly grab the least frequency used DLL
    - self.freqList to save the DLLs
"""
# Class to implement LFU cache
class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.minFreq = 0
        self.nodeMap = {} # { key : node }
        self.freqList = {} # { freq : DLL }

    # Method to update frequency of data-items
    def updateFreqListMap(self, node):
        # check if the item we move is the last one in the DLL, then we need to update minFreq
        # but only if the current DLL is the minFreq + this is the last node in the DLL

        current_dll = self.freqList[node.cnt]
        current_dll.removeNode(node)

        if node.cnt == self.minFreq and current_dll.size == 0:
            self.minFreq += 1

        # change freq
        node.cnt += 1

        if node.cnt not in self.freqList:
            self.freqList[node.cnt] = List()

        self.freqList[node.cnt].addFront(node)

    # Method to get the value of key from LFU cache
    def get(self, key):
        if key in self.nodeMap:
            node = self.nodeMap[key]
            self.updateFreqListMap(node)
            return node.value
        else:
            return -1

    def put(self, key, value):
        if self.capacity == 0: return

        if key in self.nodeMap:
            node = self.nodeMap[key]
            node.value = value
            self.updateFreqListMap(node)
            return

        # remove LFU if over capacity
        if len(self.nodeMap) == self.capacity:
            lfu_node = self.freqList[self.minFreq].tail.prev
            self.freqList[self.minFreq].removeNode(lfu_node)
            del self.nodeMap[lfu_node.key]

        new_node = Node(key, value)
        self.minFreq = 1

        if 1 not in self.freqList:
            self.freqList[1] = List()

        self.freqList[1].addFront(new_node)
        self.nodeMap[key] = new_node

# LFU Cache
cache = LFUCache(2)

# [(1 : 1), (2 : 2), (3, 3)

# Queries
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1), end=" ")
cache.put(3, 3)
print(cache.get(2), end=" ")
print(cache.get(3), end=" ")
cache.put(4, 4)
print(cache.get(1), end=" ")
print(cache.get(3), end=" ")
print(cache.get(4), end=" ")