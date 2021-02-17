l = [1, 2, 3, 4, 5, 6, 7]
nl = []
while l:
    nl.append(l.pop())
print(nl)

class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False










