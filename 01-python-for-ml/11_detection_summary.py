from pprint import pprint

# detection summary
def detection_summary(detections):
    if not detections:
        return {}

    results = {}

    # total number of detections
    results["Total detections"] = len(detections)

    # number of unique detections
    unique = []
    for detection in detections:
        if detection["object"] not in unique:
            unique.append(detection["object"])

    results["Unique objects are"] = len(unique)

    # highest confidence
    for det in detections:
        high = det["confidence"]
        break

    for detection in detections:
        if detection["confidence"] > high:
            high = detection["confidence"]

    results["Highest confidence"] = high

    #lowest confidence 
    for det in detections:
        low = det["confidence"]
        break

    for detection in detections:
        if detection["confidence"] < low:
            low = detection["confidence"]

    results["Lowest confidence"] = low

    # average confidence
    total = 0
    for detection in detections:
        total += detection["confidence"]

    average = total / len(detections)
    results["Average confidence"] = average

    return results

# main program
detections = [
    {"object": "person", "confidence": 0.91},
    {"object": "car", "confidence": 0.72},
    {"object": "person", "confidence": 0.87},
    {"object": "dog", "confidence": 0.81},
    {"object": "car", "confidence": 0.94},
    {"object": "person", "confidence": 0.55},
    {"object": "dog", "confidence": 0.76},
    {"object": "bird", "confidence": 0.88}
]

pprint(detection_summary(detections), sort_dicts = False)
