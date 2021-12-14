import random


class RandomizedSet:
    def __init__(self):
        self.set = set()

    def insert(self, val):
        if val in self.set:
            return False
        else:
            self.set.add(val)
            return True

    def remove(self, val):
        if val not in self.set:
            return False
        else:
            self.set.remove(val)
            return True

    def GetRandom(self):
        return random.choice(list(self.set))


rset = RandomizedSet()


print(rset.insert(1), rset.remove(2), rset.insert(2), rset.GetRandom(), rset.remove(1), rset.insert(2),
     rset.GetRandom())
