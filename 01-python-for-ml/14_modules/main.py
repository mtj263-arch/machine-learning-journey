from pprint import pprint 
import preprocessing as pp

detections = [
    {"object": " Person ", "confidence": 91, "bbox": [120, 85, 310, 450]},
    {"object": "car", "confidence": 87, "bbox": [420, 180, 760, 390]},
    {"object": " PERSON", "confidence": 78, "bbox": [810, 95, 960, 420]},
    {"object": "truck ", "confidence": 94, "bbox": [50, 210, 380, 480]},
    {"object": "Car", "confidence": 82, "bbox": [600, 300, 890, 510]},
    {"object": " bicycle ", "confidence": 76, "bbox": [250, 320, 410, 500]},
    {"object": "DOG", "confidence": 88, "bbox": [470, 350, 610, 500]},
    {"object": "person", "confidence": 96, "bbox": [930, 70, 1090, 430]},
    {"object": " motorcycle ", "confidence": 83, "bbox": [700, 260, 880, 470]},
    {"object": "car ", "confidence": 89, "bbox": [1000, 190, 1230, 410]},

    {"object": "Bird", "confidence": 72, "bbox": [80, 40, 150, 110]},
    {"object": " PERSON ", "confidence": 93, "bbox": [340, 100, 500, 440]},
    {"object": "bus", "confidence": 97, "bbox": [520, 120, 900, 430]},
    {"object": "cat ", "confidence": 81, "bbox": [180, 380, 300, 490]},
    {"object": "CAR", "confidence": 74, "bbox": [910, 250, 1190, 470]},
    {"object": "truck", "confidence": 86, "bbox": [30, 300, 330, 520]},
    {"object": " dog ", "confidence": 91, "bbox": [450, 280, 590, 470]},
    {"object": "person", "confidence": 84, "bbox": [650, 80, 790, 410]},
    {"object": "BICYCLE", "confidence": 79, "bbox": [820, 330, 970, 510]},
    {"object": " motorcycle", "confidence": 90, "bbox": [1040, 290, 1210, 500]},

    {"object": "car", "confidence": 95, "bbox": [100, 180, 390, 390]},
    {"object": " Person", "confidence": 73, "bbox": [400, 70, 540, 420]},
    {"object": "bus ", "confidence": 92, "bbox": [580, 150, 940, 450]},
    {"object": "DOG ", "confidence": 85, "bbox": [970, 350, 1110, 500]},
    {"object": "truck", "confidence": 80, "bbox": [720, 100, 1030, 390]},
    {"object": "cat", "confidence": 77, "bbox": [120, 400, 240, 510]},
    {"object": " CAR ", "confidence": 88, "bbox": [300, 240, 570, 430]},
    {"object": "bird ", "confidence": 69, "bbox": [1080, 60, 1160, 130]},
    {"object": "person", "confidence": 98, "bbox": [600, 60, 750, 440]},
    {"object": "motorcycle", "confidence": 75, "bbox": [850, 270, 1010, 480]},

    {"object": "TRUCK", "confidence": 89, "bbox": [20, 180, 350, 450]},
    {"object": " bicycle", "confidence": 83, "bbox": [370, 340, 520, 510]},
    {"object": "Person ", "confidence": 90, "bbox": [550, 90, 700, 430]},
    {"object": "car", "confidence": 71, "bbox": [760, 200, 1040, 420]},
    {"object": "DOG", "confidence": 87, "bbox": [1050, 330, 1190, 510]},
    {"object": " bus", "confidence": 93, "bbox": [150, 100, 500, 380]},
    {"object": "CAT", "confidence": 80, "bbox": [530, 390, 650, 510]},
    {"object": " motorcycle ", "confidence": 84, "bbox": [690, 290, 850, 490]},
    {"object": "CAR ", "confidence": 92, "bbox": [880, 170, 1160, 410]},
    {"object": "bird", "confidence": 68, "bbox": [450, 30, 530, 100]}
]

processed_dataset = []

for det in detections:
    processed_detection = {
        "object": pp.clean_label(det["object"]),
        "confidence": pp.normalize_confidence(det["confidence"]),
        "bbox": det["bbox"]
    }

    processed_dataset.append(processed_detection)

pprint(processed_dataset, sort_dicts = False)
