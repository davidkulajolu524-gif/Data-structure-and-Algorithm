# Name: Kulajolu David
# Matric Number: 240502063
# Course of Study: Computer Science

# Assignment 1: Array Operations in Python

# Creating an array containing the examination
# results of eight students.

scores = [78, 85, 62, 91, 73, 88, 56, 80]

# 1. Displaying the original array
print("=== INITIAL ARRAY ===")
print("Student Scores:", scores)
print("Total Elements:", len(scores))

# 2. Traversing the array
print("\n=== ARRAY TRAVERSAL ===")
for index, score in enumerate(scores):
    print(f"Index {index}: {score}")

# 3. Retrieving elements using their positions
print("\n=== ACCESSING ARRAY ELEMENTS ===")
print("Score at the first position:", scores[0])
print("Score at the fifth position:", scores[4])

# 4. Adding new elements to the array
print("\n=== INSERTION OPERATION ===")
scores.append(94)
scores.insert(3, 76)
print("Array after insertion:", scores)

# 5. Modifying an existing element
print("\n=== UPDATING ARRAY ELEMENT ===")
scores[2] = 70
print("Modified array:", scores)

# 6. Locating a particular value
print("\n=== SEARCH OPERATION ===")
target = 88

if target in scores:
    print("Value", target, "exists at index", scores.index(target))
else:
    print("The requested value does not exist.")

# 7. Removing elements from the array
print("\n=== DELETION OPERATION ===")
scores.remove(56)
deleted_score = scores.pop(4)

print("Deleted element:", deleted_score)
print("Array after deletion:", scores)

# 8. Arranging elements in ascending and descending order
print("\n=== SORTING AND REVERSING ===")
scores.sort()
print("Ascending order:", scores)

scores.reverse()
print("Descending order:", scores)

# Displaying the final number of elements
print("\n=== FINAL ARRAY INFORMATION ===")
print("Final Scores:", scores)
print("Total Elements Remaining:", len(scores))