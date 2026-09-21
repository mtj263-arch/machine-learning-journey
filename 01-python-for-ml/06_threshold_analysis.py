# Find values above threshold
def above_threshold(scores, threshold):
    results = []

    for score in scores:
        if score >= threshold:
            results.append(score)

    return f'\nValues above threshold: {results}'

# Find values below threshold
def below_threshold(scores, threshold):
    results = []

    for score in scores:
        if score < threshold:
            results.append(score)

    return f"Values below threshold: {results}"

# Percentage of values above threshold
def percentage_above_threshold(scores, threshold):
    count = 0

    for score in scores:
        if score >= threshold:
           count += 1

    percent = (count / len(scores)) * 100

    return f"{percent}% values are above threshold ({threshold})"


# Main Program
threshold = 0.80
confidence_scores = [
    0.42,
    0.87,
    0.91,
    0.63,
    0.78,
    0.95,
    0.51,
    0.84
]

print(above_threshold(confidence_scores, threshold))
print(below_threshold(confidence_scores, threshold))
print(percentage_above_threshold(confidence_scores, threshold))
