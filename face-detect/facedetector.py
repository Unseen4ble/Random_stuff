import cv2
import os
from frameex import extractor

# emptying split frame folder
input_folder = "split_frames"
output_folder = "detected_frames"

for item in os.listdir(input_folder):
    item_path = os.path.join(input_folder, item)
    if os.path.isfile(item_path):
        os.remove(item_path) 

for item in os.listdir(output_folder):
    item_path = os.path.join(output_folder, item)
    if os.path.isfile(item_path):
        os.remove(item_path) 

#extracting frame
temp1=extractor("video.mp4")
temp1.extract()

os.makedirs(output_folder, exist_ok=True)

image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

saved_count = 0
# Load face detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

#face detection stuff
for image_name in image_files:
    image_path = os.path.join(input_folder, image_name)
    frame = cv2.imread(image_path)
    
    if frame is None:
        print(f"Could not read {image_path}, skipping.")
        continue

    try:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        if len(faces) > 0:
            saved_count += 1
            output_path = os.path.join(output_folder, image_name)
            cv2.imwrite(output_path, frame)
            print(f"{image_name}: {len(faces)} face(s) detected and saved.")

    except Exception as e:
        print(f"Error in {image_name}: {e}")

print(f"Detection complete. {saved_count} frames saved in '{output_folder}'")