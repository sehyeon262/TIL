front = rear = -1
q = [0] * 10

# enq(1)
rear += 1
q[rear] = 1
# enq(2)
rear += 1
q[rear] = 2
# enq(3)
rear += 1
q[rear] = 3

# deq()
front += 1
print(q[front])
# deq()
front += 1
print(q[front])
# deq()
front += 1
print(q[front])



