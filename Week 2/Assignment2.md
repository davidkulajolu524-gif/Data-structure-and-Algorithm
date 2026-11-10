Assignment 2: Queue Data Structure

Name: Kulajolu David
Matric Number: 240502063
Course of Study: Computer Science

A Queue works on the FIFO (First-In, First-Out) rule. It works just like a line of students waiting at the cafeteria: the first person to join the line is the first person to get served and leave.

Simple Algorithm for Queue Operations
Initialize Queue: Create an empty list called queue and set a maximum size max_size.

isEmpty Operation:

Check if len(queue) == 0. If yes, the queue is empty.

isFull Operation:

Check if len(queue) == max_size. If yes, the queue is full.

Enqueue Operation (Adding an item to the back/rear):

Step 1: Check if the queue is full. If it is full, print "Queue is Full (Overflow)" and stop.

Step 2: If not full, add the new item to the end of the queue.

Dequeue Operation (Removing an item from the front):

Step 1: Check if the queue is empty. If it is empty, print "Queue is Empty (Underflow)" and stop.

Step 2: If not empty, remove and return the item at index 0 (the front).

Peek / Front Operation:

Check if the queue is empty. If not, show the first item (queue[0]) without removing it.

Rear Operation:

Check if the queue is empty. If not, show the last item (queue[-1]) without removing it.

Display Operation:

Print all items currently inside the queue from front to back.