class RandomizedSet:

    def __init__(self):
        self.list = []
        self.dict = {}

    def insert(self, val: int) -> bool:
        if not val in self.dict:
            self.list.append(val)
            self.dict[val] = len(self.list) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.dict:
            val_idx = self.dict.pop(val)
            last_val = self.list[-1]

            if val_idx != len(self.list) - 1:
                self.dict[last_val] = val_idx
                self.list[val_idx] = last_val

            self.list.pop()
            return True
        return False        

    def getRandom(self) -> int:
        return random.choice(self.list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()