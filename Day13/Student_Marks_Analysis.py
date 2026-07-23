import numpy as np

print("===== Student Marks Analysis =====")

# Store marks using NumPy array
marks = np.array([85, 92, 76, 88, 95])

print("\nStudent Marks:")
print(marks)

# Total Marks
print("\nTotal Marks:", np.sum(marks))

# Average Marks
print("Average Marks:", np.mean(marks))

# Highest Marks
print("Highest Marks:", np.max(marks))

# Lowest Marks
print("Lowest Marks:", np.min(marks))
