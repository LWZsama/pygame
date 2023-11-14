class queue():
    def __init__(self,data):
        self.data=data
    
    def enQueue(self,element):
        self.data.append(element)

    def deQueue(self):
        copy=self.data[0]
        self.data.pop(0)
        return copy
    
q=queue([])
q.enQueue(1)
q.enQueue(2)
q.enQueue(3)

print(q.deQueue())
