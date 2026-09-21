# Cleaning detections 
def clean_detections(detections):
    results = []

    for detection in detections:
        detection = detection.strip()
        if detection != "":
            results.append(detection.lower())

    return results

# Filtering unique detections
def unique_detections(detections):
    unique = []

    for detection in detections:
        if detection not in unique:
            unique.append(detection)

    return unique


# Main program
detections = [
    "person",
    " car",
    "PERSON",
    "",
    "dog ",
    "car",
    " person ",
    "",
    "DOG",
    "bird"
]

print(f"\nDetections recorded: {detections}")
print("Cleaned detections: ", clean_detections(detections))

cleaned = clean_detections(detections)
print("Unique detections: ", unique_detections(cleaned))
