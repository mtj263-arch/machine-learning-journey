from pprint import pprint

detections = [
    "person,0.91",
    "car,0.72",
    "dog,invalid",
    "person,0.87",
    "bird,0.88",
    "car,",
    "cat,0.76"
]

results = []
rejected_count = 0

for det in detections:
    line = det.split(",")
    try:
        line_dict = {
        "object": line[0], "confidence": float(line[1])
        }
        results.append(line_dict)

    except (ValueError, IndexError):
        rejected_count += 1
        continue

pprint(results, sort_dicts = False)
print(f"{rejected_count} values are rejected")
