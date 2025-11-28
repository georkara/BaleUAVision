import cv2
import os
import json
import numpy as np
from PIL import Image as PILImage
import random

# Specify paths
images_dir = r'E:\BaleUAVision\Annotated Data\Hay bales 10\images'
json_file_path = r'E:\BaleUAVision\Annotated Data\Hay bales 10\Hay-bales-10-JSON.json'
output_dir = r'E:\BaleUAVision\Annotations Visualization\Hay bales 10\visualized_json'

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to draw both bounding boxes, filled polygons with transparency, and labels
def draw_annotations(image_path, annotations, output_path):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Failed to load image: {image_path}")
        return

    # Draw each annotation
    for annotation in annotations:
        if annotation['type'] == 'polygonlabels':
            points = annotation['value']['points']
            # Scale points to match image size
            height, width = image.shape[:2]
            scaled_points = [(int(x * width / 100), int(y * height / 100)) for x, y in points]
            points_array = np.array(scaled_points, dtype=np.int32)

            # Generate a random color
            color = tuple(random.randint(0, 255) for _ in range(3))

            # Draw filled polygon with transparency
            overlay = image.copy()
            cv2.fillPoly(overlay, [points_array], color)
            cv2.addWeighted(overlay, 0.5, image, 0.5, 0, image)

            # Draw bounding box
            x, y, w, h = cv2.boundingRect(points_array)
            cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

            # Add label above the bounding box
            label = annotation['value'].get('polygonlabels', ['Unknown'])[0]
            cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Save the annotated image with '_annotated' suffix
    annotated_image_name = os.path.basename(image_path).replace('.JPG', '_annotated.JPG')
    output_path = os.path.join(output_dir, annotated_image_name)
    cv2.imwrite(output_path, image)
    print(f"Saved annotated image to: {output_path}")

# Load JSON data
with open(json_file_path, 'r') as file:
    data = json.load(file)

# Process each labeled image
for task in data:
    image_file_name = os.path.basename(task['data']['image'])
    image_path = os.path.join(images_dir, image_file_name)

    if not os.path.exists(image_path):
        print(f"Image file not found: {image_path}")
        continue

    # Get annotations
    annotations = task['annotations'][0]['result']

    # Define output path with '_annotated' suffix
    output_image_path = os.path.join(output_dir, image_file_name.replace('.JPG', '_annotated.JPG'))

    # Draw annotations and save
    draw_annotations(image_path, annotations, output_image_path)
