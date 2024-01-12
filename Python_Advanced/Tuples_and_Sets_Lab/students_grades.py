n = int(input())

grades = {}

for _ in range(n):
    name, grade_str = input().split()
    grade = float(grade_str)

    if name not in grades:
        grades[name] = []
    grades[name].append(grade)

for name, grades in grades.items():
    avg_grade = sum(grades)/len(grades)
    format_grades = f"{' '.join([f'{g:.2f}' for g in grades])}"
    print(f"{name} -> {format_grades} (avg: {avg_grade:.2f})")