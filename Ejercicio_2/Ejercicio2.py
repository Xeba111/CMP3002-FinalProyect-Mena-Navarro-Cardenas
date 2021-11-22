import random

"""def __init__(self):

        self.elements = []
        self.index = {}

    def insert(self, val: int) -> bool:
        for v in self.index:
            if v == val:
                return False
        else:
            self.index[val] = len(self.elements)
            return True

    def Remove(self, val):
        if val not in self.index:
            return False
        else:


    def GetRandom(self) -> int:
        return random.choice(self.elements)"""


class RandomizedSet:
    def __init__(self):
        self.set = set()

    def insert(self, val):
        if val in self.set:
            return False
        else:
            self.set.add(val)
            return True

    def Remove(self, val):
        if val not in self.set:
            return False
        else:
            self.set.remove(val)
            return True

    def GetRandom(self):
        return random.choice(list(self.set))


rset = RandomizedSet()
print(rset.insert(1), rset.Remove(2), rset.insert(2), rset.GetRandom(), rset.Remove(1), rset.insert(2),
      rset.GetRandom())
