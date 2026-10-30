def quick_sort(students, low=0, high=None):
    if high is None:
        high = len(students) - 1

    if low >= high:
        return

    pivot = students[high]["marks"]
    boundary = low - 1

    for current in range(low, high):
        if students[current]["marks"] >= pivot:
            boundary += 1
            students[boundary], students[current] = (
                students[current],
                students[boundary],
            )

    pivot_index = boundary + 1
    students[pivot_index], students[high] = (
        students[high],
        students[pivot_index],
    )

    print(
        f"Pivot {pivot}: {students[low:pivot_index]} | "
        f"{students[pivot_index]} | {students[pivot_index + 1:high + 1]}"
    )

    quick_sort(students, low, pivot_index - 1)
    quick_sort(students, pivot_index + 1, high)


students = [
    {"roll": 12, "name": "Nila", "marks": 78},
    {"roll": 7, "name": "Arun", "marks": 55},
    {"roll": 19, "name": "Dev", "marks": 91},
    {"roll": 4, "name": "Sara", "marks": 68},
    {"roll": 15, "name": "Isha", "marks": 84},
]

quick_sort(students)
print("Sorted by descending marks:", students)