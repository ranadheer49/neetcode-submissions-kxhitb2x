class Node:
    def __init__(self,key,val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    
    def __init__(self, capacity: int):
        self.cap= capacity
        self.lruMap = {}
        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next, self.tail.prev = self.tail, self.head

    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next = node.next
        nxt.prev = node.prev  

    def insert(self,node):
        prev, nxt = self.tail.prev, self.tail
        prev.next = node
        node.prev = prev

        node.next = self.tail
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.lruMap:
            node = self.lruMap[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1    
        
    def put(self, key: int, value: int) -> None:
        if key in self.lruMap:
            self.remove(self.lruMap[key])

        node = Node(key,value)
        self.lruMap[key] = node
        self.insert(node)

        if len(self.lruMap) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.lruMap[lru.key]
            
      
        #  get put -> O(1)
        #  key , value -> time as criteria 
        #  map will have key value
        #  