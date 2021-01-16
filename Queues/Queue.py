class Queue(object):
    def __init__(self):
        self.queue = []

    def __len__(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def front(self):
        return None if self.is_empty() else self.queue[0]

    def back(self):
        return None if self.is_empty() else self.queue[-1]

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        front = self.front()
        self.queue.remove(front)
        return front

    def print(self):
        print('front -> ', end='')
        for i in self.queue:
            print('{0}'.format(i), end=' -> ')
        print('back')


if __name__ == "__main__":
    q = Queue()
    print(q.is_empty())
    q.enqueue('a')
    q.enqueue('b')
    q.enqueue('c')
    q.enqueue('d')
    q.print()
    print(q.is_empty())
    print(q.front())
    print(q.back())
    print(q.dequeue())
    q.print()
    print(len(q))
