from pprint import pprint


# data cleaning
def clean_data(detections):
    results = []

    for detection in detections:
        detection["object"] = detection["object"].strip().lower()

        if detection["object"] != "":
            results.append(detection)

    return results

# filtering detections above threshold
def filter_data(detections, threshold):
    results = []

    for detection in detections:
        if detection["confidence"] >= threshold:
            results.append(detection)

    return results

# count how many time objects appeared in filtered list 
def count_objects(detections):
    results = {}

    for detection in detections:
        
        if detection["object"] in results:
            results[detection["object"]] += 1
        else:
            results[detection["object"]] = 1

    return results
# calculate average confidence from filtered detections
def average_confidence(detections):
    if not detections:
        return 0.0

    total = 0
    for detection in detections:
        total += detection["confidence"]

    return total / len(detections)


# main program
threshold = 0.80
detections = [
    {"object": " Person ", "confidence": 0.91},
    {"object": "car", "confidence": 0.72},
    {"object": "PERSON", "confidence": 0.87},
    {"object": "", "confidence": 0.65},
    {"object": " dog ", "confidence": 0.81},
    {"object": "CAR", "confidence": 0.94},
    {"object": "person", "confidence": 0.55},
    {"object": "DOG", "confidence": 0.76}
]

cleaned = clean_data(detections)
print("\nCleaned detections: ")
pprint(cleaned, sort_dicts = False)

filtered = filter_data(cleaned, threshold)
print("\nDetection above/equal to threshold: ")
pprint(filtered, sort_dicts = False)

counts = count_objects(filtered)
print(f"\nHow many times each object appeared: {counts}")


average = average_confidence(filtered)
print(f"\nAverage confidence: {average}")
