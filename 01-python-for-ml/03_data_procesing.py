confidence_scores = [0.72, 0.91, 0.45, 0.83, 0.67, 0.95, 0.58, 0.79]

# Average Calculation
def average_score(scores):
    average = sum(scores)/len(scores)
    return average

# Find Minimum Score
def min_score(scores):
    low = scores[0]

    for score in scores:
        if score < low:
            low = score

    return low

# Find Maximum score 
def max_score(scores):
    high = scores[0]

    for score in scores:
        if score > high:
            high = score

    return high

# FInd Value Above Threshold
def above_threshold(scores, threshold):
    count = 0
    for score in scores:
        if score >= threshold:
            count += 1

    return count

# Function Calling 
print("\nAverage Score is: ", average_score(confidence_scores))
print("Minimum Score is: ", min_score(confidence_scores))
print("Maximum score is: ", max_score(confidence_scores))
print("Number of Values Above Threshold (0.75): ", above_threshold(confidence_scores, 0.75))
