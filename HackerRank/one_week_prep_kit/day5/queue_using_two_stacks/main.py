from collections import deque

# Read the number of queries
q = int(input().strip())

# Create a deque object to represent the queue
queue = deque()

# Process each query
for _ in range(q):
    query = list(map(int, input().strip().split()))
    query_type = query[0]

    if query_type == 1:
        queue.append(query[1])  # Enqueue operation
    elif query_type == 2:
        queue.popleft()  # Dequeue operation
    elif query_type == 3:
        print(queue[0] if queue else None)  # Print front element

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
