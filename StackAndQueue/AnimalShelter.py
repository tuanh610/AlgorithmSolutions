from QueueImplementation import LinklistQueue

class Animal:
    def __init__(self, name, order):
        self.name = name
        self.order = order
        
class AnimalShelter:
    def __init__(self):
        self.cats = LinklistQueue()
        self.dogs = LinklistQueue()
        self.order = 0

    def enqueueDog(self, name):
        self.order += 1
        self.dogs.enqueue(Animal(name, self.order))

    def enqueueCat(self, name):
        self.order += 1
        self.cats.enqueue(Animal(name, self.order))

    def dequeueDog(self):
        return self.dogs.dequeue()

    def dequeueCat(self):
        return self.cats.dequeue()

    def dequeueAny(self):
        if self.cats.peek() < self.dogs.peek():
            return self.cats.dequeue()
        else:
            return self.dogs.dequeue()
