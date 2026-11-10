# Name: Kulajolu David
# Matric Number: 240502063
# Course of Study: Computer Science

# Assignment 2: Queue Implementation in Python
# FIFO = First-In, First-Out

queue = []
max_size = 5  # Maximum number of items our queue can hold

# 1. Check if queue is empty
def is_empty():
    return len(queue) == 0

# 2. Check if queue is full
def is_full():
    return len(queue) == max_size

# 3. Enqueue: Add an item to the back (rear) of the queue
def enqueue(item):
    if is_full():
        print("Queue is Full! Cannot add:", item)
    else:
        queue.append(item)
        print(item, "has been added to the queue.")

# 4. Dequeue: Remove an item from the front of the queue
def dequeue():
    if is_empty():
        print("Queue is Empty! Nothing to remove.")
    else:
        removed = queue.pop(0)  # pop(0) removes the very first item
        print(removed, "has been removed from the front of the queue.")

# 5. Peek / Front: See who is at the front without removing them
def front():
    if is_empty():
        print("Queue is Empty!")
    else:
        print("Front element is:", queue[0])

# 6. Rear: See who is at the back of the queue
def rear():
    if is_empty():
        print("Queue is Empty!")
    else:
        print("Rear element is:", queue[-1])

# 7. Size: Get the total number of items in the queue
def size():
    print("Current queue size is:", len(queue))

# 8. Display: Show the whole queue
def display():
    if is_empty():
        print("Queue is currently empty: []")
    else:
        print("Current Queue (Front to Rear):", queue)


# --- Testing all the Queue Operations ---
print("--- Starting Queue Operations ---")
print("Is the queue empty right now?", is_empty())

print("\n--- Adding items (Enqueue) ---")
enqueue("Student 1")
enqueue("Student 2")
enqueue("Student 3")
enqueue("Student 4")
enqueue("Student 5")
enqueue("Student 6")  # This will show Queue is Full because max_size is 5

print("\n--- Checking Queue Details ---")
display()
front()
rear()
size()
print("Is the queue full?", is_full())

print("\n--- Removing items (Dequeue) ---")
dequeue()  # Removes Student 1
dequeue()  # Removes Student 2

print("\n--- Final Queue State ---")
display()
front()
rear()
size()