results = []

with open("detections.txt") as dets:

    for det in dets:
        line = det.strip().split(",")       
        line_dict = {
            "object": line[0], "confidence": float(line[1])
            }

        results.append(line_dict)

print(results)
