# Filtering Scores Above Threshold
def high_scores(scores, threshold):
    high = []

    for score in scores:
        if score >= threshold:
            high.append(score)

    return high

#filtering Scores Below Threshold
def low_scores(scores, threshold):
    low = []

    for score in scores:
        if score < threshold:
            low.append(score)

    return low

# Main Program

confidence_scores = [0.32, 0.87, 0.91, 0.45, 0.76, 0.63, 0.98, 0.54, 0.82]
threshold = 0.80

high = high_scores(confidence_scores, threshold)
low = low_scores(confidence_scores, threshold)

print("\nRecorded Confidence Scores: ", confidence_scores)
print("Number Confidence Scores: ", len(confidence_scores))

print("\nConfidence Scores Above/Equal Threshold: ", high)
print("Number of Values Above/Equal Threshold: ", len(high))

print("\nConfidence Scores Below Threshold: ", low)
print("Number of Values Below Threshold: ", len(low))
