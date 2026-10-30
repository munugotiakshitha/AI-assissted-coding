def merge_sort(records, depth=0):
    indent = "  " * depth

    if len(records) <= 1:
        return records

    middle = len(records) // 2
    left = records[:middle]
    right = records[middle:]

    print(f"{indent}Split: {left} | {right}")

    left = merge_sort(left, depth + 1)
    right = merge_sort(right, depth + 1)

    merged = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i]["bill"] <= right[j]["bill"]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    merged.extend(left[i:])
    merged.extend(right[j:])

    print(f"{indent}Merge: {merged}")
    return merged


patients = [
    {"id": 101, "name": "Asha", "bill": 7500},
    {"id": 102, "name": "Ravi", "bill": 3200},
    {"id": 103, "name": "Meera", "bill": 8900},
    {"id": 104, "name": "Kabir", "bill": 4100},
]

sorted_patients = merge_sort(patients)
print("Sorted by bill:", sorted_patients)