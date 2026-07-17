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

# Class to implement LFU cache
class LFUCache:
    def __init__(self, capacity):
        self.maxSizeCache = capacity
        self.minFreq = 0
        self.curSize = 0
        
        self.cache = {} # {key : node}
        
        self.freqListMap = {} # {freq : DLL}
        
    # Method to update frequency of data-items
    def updateFreqListMap(self, node):
        del self.cache[node.key]
        
        # set freqlistMap
        self.freqListMap[node.cnt].removeNode(node)
        
        if (node.cnt == self.minFreq and self.freqListMap[node.cnt].size == 0):
            self.minFreq += 1
            
        nextHigherFreqList = List()
        if node.cnt + 1 in self.freqListMap:
            nextHigherFreqList = self.freqListMap[node.cnt + 1]
        
        node.cnt += 1
        nextHigherFreqList.addFront(node)
        
        self.freqListMap[node.cnt] = nextHigherFreqList
        self.cache[node.key] = node

    # Method to get the value of key from LFU cache
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            
            # remove the node from the list, update the freq list
            self.updateFreqListMap(node)
            
            return node.value
        else:
            return -1

    def put(self, key, value):
        if self.maxSizeCache == 0:
            return
        
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self.updateFreqListMap(node)
        else:
            if self.curSize == self.maxSizeCache:
                l = self.freqListMap[self.minFreq]
                del self.cache[l.tail.prev.key]
                
                self.freqListMap[self.minFreq].removeNode(l.tail.prev)
                self.curSize -= 1
                
            self.curSize += 1
            self.minFreq = 1
            
            listFreq = List()
            
            if self.minFreq in self.freqListMap:
                listFreq = self.freqListMap[self.minFreq]
                
            new_node = Node(key, value)
            self.cache[key] = new_node
            listFreq.addFront(new_node)
            
            self.freqListMap[self.minFreq] = listFreq

# LFU Cache
cache = LFUCache(2)

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
