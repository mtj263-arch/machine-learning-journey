# extract scores
def get_scores(students):
    scores = []

    for student in students:
        scores.append(student["score"])

    return scores

# filter students having score higher or equal to threshold
def filter_students(students, threshold):
    filtered = []

    for student in students:
        if student["score"] >= threshold:
            filtered.append(student)

    return filtered

# counting students belonging to each field
def field_counts(students):
    counts = {}

    for student in students:
        if student["field"] in counts:
            counts[student["field"]] += 1
        else:
            counts[student["field"]] = 1

    return counts


# main program
threshold = 80
students = [
    {
        "name": "Ali",
        "score": 85,
        "field": "AI"
    },
    {
        "name": "Sara",
        "score": 72,
        "field": "Data Science"
    },
    {
        "name": "Ahmed",
        "score": 91,
        "field": "AI"
    },
    {
        "name": "Maria",
        "score": 64,
        "field": "ML"
    },
    {
        "name": "David",
        "score": 78,
        "field": "AI"
    }
]

scores = get_scores(students)
print(f"\nScores: {scores}")

filtered = filter_students(students, threshold)
print(f"Students having scores above/equall {threshold}: {filtered}")

counts = field_counts(students)
print(f"Students in each field: {counts}")
