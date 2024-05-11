class QueueWithTwoStacks:
    def __init__(self):
        self.stack1 = []  # For enqueue operation
        self.stack2 = []  # For dequeue operation

    def enqueue(self, x):
        self.stack1.append(x)

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            self.stack2.pop()

    def front(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if self.stack2:
            return self.stack2[-1]
        elif self.stack1:
            return self.stack1[-1]
        else:
            return None


# Read the number of queries
q = int(input().strip())

# Create a queue object
queue = QueueWithTwoStacks()

# Process each query
for _ in range(q):
    query = list(map(int, input().strip().split()))
    query_type = query[0]

    if query_type == 1:
        queue.enqueue(query[1])
    elif query_type == 2:
        queue.dequeue()
    elif query_type == 3:
        print(queue.front())

"""Test Input 1
10
1 42
2
1 14
3
1 28
3
1 60
1 78
2
2
"""
