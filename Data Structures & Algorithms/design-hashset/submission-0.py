class MyHashSet:

    def __init__(self):
        self.num_buckets=1000
        self.buckets=[[] for _ in range(0,1000)]
    
    def hash_func(self,key):
        return key%self.num_buckets
    
    def add(self, key: int) -> None:
        buck=self.hash_func(key)
        if key not in self.buckets[buck]:
            self.buckets[buck].append(key)


    def remove(self, key: int) -> None:
        buck=self.hash_func(key)
        if key in self.buckets[buck]:
            self.buckets[buck].remove(key)
        

    def contains(self, key: int) -> bool:
        buck=self.hash_func(key)
        return key in self.buckets[buck]

        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)