# List Unique Objects 
def unique_objects(detections):
    unique = []

    for detection in detections:
        if detection not in unique:
            unique.append(detection)

    return unique

# Count Number of Times Each Object Appears
def count_objects(detections):
    results = {}

    for detection in detections:
        if detection in results:
            results[detection] += 1
        else:
            results[detection] = 1

    return results

# Find Most Common Objects 
def common_object(detections):
    results = {}

    for detection in detections:
        if detection in results:
            results[detection] += 1
        else:
            results[detection] = 1

    count = 0
    most_repeated = []

    for key in results:
        if results[key] > count:
            count = results[key]

    for key in results:
        if results[key] == count:
            most_repeated.append(key)

    return f'"{most_repeated}" is Repeated Mostly: {count} Times'

# Main Program

detections = [
    "person",
    "car",
    "person",
    "dog",
    "car",
    "person",
    "bird",
    "dog",
    "car"
]

print("\nDetection Results: ", detections)
print("\nDetections After Removing Duplicates: ", unique_objects(detections))
print("Number of Time Each Object Apears: ", count_objects(detections))
print(common_object(detections), end = "\n\n")
