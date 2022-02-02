class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        self.queue.append(item)
    def dequeue(self):
        if len(self.queue) == 0:
            return None
        else:
            return self.queue.pop(0)
    def display(self):
        print(self.queue)

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.dequeue()
q.display()