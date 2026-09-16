scores_list = [77, 56, 68, 84, 97]

# Highest score calculatoin
def highest_score(scores):
    high = scores_list[0]
    for score in scores:
        if score > high :
            high = score

    return high

# Average Score Calculation
def average_score(scores):
    average = sum(scores)/len(scores)
    return average


# Classify Score 
def classify_score(score):

    if 90 <= score <= 100:
        classification = 'Excellent'
    elif 80 <= score < 90:
        classification = 'Very Good'
    elif 70 <= score < 80:
        classification = 'Good'
    elif 60 <= score < 70:
        classification = 'Average'
    else:
        classification = 'Needs Improvement'

    return classification

# Calling Functions 
highest = highest_score(scores_list)
average = average_score(scores_list)
classification = classify_score(average)

print("Highest Score is: ", highest)
print("Average Score is: ", average)
print("Performance: ", classification)
