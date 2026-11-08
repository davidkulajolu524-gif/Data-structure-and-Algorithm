# Assignment 1: Array Operations in Python

# Name: Olatimilehin Majesty Oluwakolade
# Matric Number: 240502090
# Course of Study: Computer Science

# Using an array of test scores for a class size of 8 students:

# Creating the array (using a Python list as an array of integers)
class_scores = [65, 72, 80, 55, 90, 68, 75, 84]

print("--- 1. Original Array ---")
print("Scores:", class_scores)
print("Number of students (size):", len(class_scores))

# 2. Traversal (looping through and printing each item one by one)
print("\n--- 2. Traversing the Array ---")
for i in range(len(class_scores)):
    print("Student at index", i, "scored:", class_scores[i])

# 3. Accessing an element by index
print("\n--- 3. Accessing Elements ---")
print("First student's score:", class_scores[0])
print("Fourth student's score:", class_scores[3])

# 4. Insertion (adding new scores)
print("\n--- 4. Inserting Elements ---")
class_scores.append(95)        # Adds 95 to the end of the array
class_scores.insert(2, 77)     # Inserts 77 at index 2
print("Array after adding 95 and 77:", class_scores)

# 5. Updating (changing an existing score)
print("\n--- 5. Updating an Element ---")
# Changing the score at index 4 (from 55 to 60)
class_scores[4] = 60
print("Array after changing index 4 to 60:", class_scores)

# 6. Searching for an element
print("\n--- 6. Searching for an Element ---")
search_value = 90
if search_value in class_scores:
    position = class_scores.index(search_value)
    print("Score", search_value, "was found at index:", position)
else:
    print("Score not found in the array.")

# 7. Deletion (removing elements)
print("\n--- 7. Deleting Elements ---")
class_scores.remove(65)        # Removes the value 65 from the array
removed_item = class_scores.pop(3)  # Removes the item at index 3
print("Removed item at index 3:", removed_item)
print("Array after deletions:", class_scores)

# 8. Sorting and Reversing the array
print("\n--- 8. Sorting and Reversing ---")
class_scores.sort()
print("Sorted from lowest to highest:", class_scores)

class_scores.reverse()
print("Reversed (highest to lowest):", class_scores)