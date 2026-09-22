# cleaning data 
def data_cleaning(detections):
    results = []

    for detection in detections:
        detection = detection.strip()

        if detection != "":
            results.append(detection.lower())

    return results

# counting number of times objects are detected 
def count_objects(detections):
    results = {}

    for detection in detections:
        if detection in results:
            results[detection] += 1
        else:
            results[detection] = 1

    return results

# finding most common objects appeared 
def most_common_objects(counts):
    count = 0
    most_common = []

    for key in counts:
        if counts[key] > count:
            count = counts[key]

    for key in counts:
        if counts[key] == count:
            most_common.append(key)

    return most_common, count

# main program
detections = [
    "Person",
    "CAR",
    " person",
    "Dog ",
    "car",
    "BIRD",
    " dog",
    "person ",
    "Car"
]

clean = data_cleaning(detections)
counting = count_objects(clean)
mostly_appeared, count = most_common_objects(counting)

print(f"\nDetections recorded: {detections}")
print(f"Cleaned detections: {clean}")
print(f"How many times each object appears: {counting}")
print(f"{mostly_appeared} Appeared mostly: {count} times")
