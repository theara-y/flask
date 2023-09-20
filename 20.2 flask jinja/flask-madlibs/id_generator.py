class IdGenerator:
    def __init__(self):
        self.next = 0

    def newId(self):
        currentId = self.next
        self.next += 1
        return currentId

genId = IdGenerator()
