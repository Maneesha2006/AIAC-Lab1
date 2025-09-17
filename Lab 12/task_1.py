import random
import time

# Generate sample student data
def generate_students(n):
    students = []
    for i in range(n):
        name = f"Student_{i+1}"
        roll_no = f"SR{i+1000}"
        cgpa = round(random.uniform(5.0, 10.0), 2)
        students.append((name, roll_no, cgpa))
    return students

# Quick Sort by CGPA (descending)
def quick_sort(students):
    if len(students) <= 1:
        return students
    pivot = students[0][2]
    left = [s for s in students[1:] if s[2] > pivot]
    right = [s for s in students[1:] if s[2] <= pivot]
    return quick_sort(left) + [students[0]] + quick_sort(right)

# Merge Sort by CGPA (descending)
def merge_sort(students):
    if len(students) <= 1:
        return students
    mid = len(students) // 2
    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])
    return merge(left, right)

def merge(left, right):
    sorted_list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][2] > right[j][2]:
            sorted_list.append(left[i])
            i += 1
        else:
            sorted_list.append(right[j])
            j += 1
    sorted_list.extend(left[i:])
    sorted_list.extend(right[j:])
    return sorted_list

# Compare runtime performance
def compare_performance():
    students = generate_students(10000)

    start_qs = time.time()
    sorted_qs = quick_sort(students)
    end_qs = time.time()

    start_ms = time.time()
    sorted_ms = merge_sort(students)
    end_ms = time.time()

    print(f"\nQuick Sort Time: {end_qs - start_qs:.4f} seconds")
    print(f"Merge Sort Time: {end_ms - start_ms:.4f} seconds")

# Output top 10 students
def top_10_students(sorted_students):
    print("\nTop 10 Students by CGPA:")
    for i, student in enumerate(sorted_students[:10], start=1):
        print(f"{i}. Name: {student[0]}, Roll No: {student[1]}, CGPA: {student[2]}")

# Main execution
if __name__ == "__main__":
    students = generate_students(10000)

    # Quick Sort
    sorted_qs = quick_sort(students)
    top_10_students(sorted_qs)

    # Merge Sort
    sorted_ms = merge_sort(students)

    # Compare Performance
    compare_performance()