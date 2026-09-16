# LIST 

students = ["Ali", "David", "Johnson", "Travis", "Ben"]
students.append("Samir")
students.remove("Ben")
print("\nStudents: ", students)
print("First Student: ", students[0])
print("Last Student In List: ", students[-1])

# Tuple

image_size = (1280, 720)

# UNPACKING
width, height = image_size
print("\nUnpacked Width: ", width)
print("Unpacked Height: ", height)

# DICTIONARY

student = {
    "Name": "Ali",
    "Age": 22,
    "Field": "Artificial Intelligence",
    "CGPA": 3.15
}

# Adding a Key in Dictionary
student["University"] = "The Islamia University of Bahawalpur"

# Updating a Key
student["CGPA"] = 3.40

# Fetching Data From Dictionary
print("\nName: ", student["Name"])
print("Field: ", student["Field"], end = "\n\n")

# Printing all key-values
for key, value in student.items():
    print(key, ":", value)

# SET

cam1_detections = {'person', 'cat', 'dog', 'bag'}
cam2_detections = {'car', 'bike', 'drone', 'person', "bag"}

print("\nCommon Objects Detected by Both Cameras: ", cam1_detections.intersection(cam2_detections))
print("All Detected Objects: ", cam1_detections.union(cam2_detections))
print("Uncommon Objects Detected By Camera 1: ", cam1_detections.difference(cam2_detections))
