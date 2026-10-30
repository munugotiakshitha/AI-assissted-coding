def bubble_sort(students):
    n = len(students)

    for pass_number in range(n - 1):
        swapped = False

        for j in range(n - 1 - pass_number):
            if students[j]["marks"] > students[j + 1]["marks"]:
                students[j], students[j + 1] = students[j + 1], students[j]
                swapped = True

        print(f"After pass {pass_number + 1}: {students}")

        if not swapped:
            break


students = [
    {"roll": 12, "name": "Nila", "marks": 78},
    {"roll": 7, "name": "Arun", "marks": 55},
    {"roll": 19, "name": "Dev", "marks": 91},
    {"roll": 4, "name": "Sara", "marks": 68},
]

bubble_sort(students)