def insertion_sort(salaries):
    for i in range(1, len(salaries)):
        key = salaries[i]
        j = i - 1

        while j >= 0 and salaries[j] > key:
            salaries[j + 1] = salaries[j]  # Shift right
            j -= 1

        salaries[j + 1] = key
        print(f"After iteration {i}: {salaries}")


salaries = [45000, 32000, 50000, 28000, 39000]
insertion_sort(salaries)