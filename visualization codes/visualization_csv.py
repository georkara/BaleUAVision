import cv2
import json
import pandas as pd
import numpy as np
import os

# Specify paths
csv_file_path = r'E:/BaleUAVision/Annotated Data/Hay bales 10/Hay-bales-10-CSV.csv'
image_dir = r'E:/BaleUAVision/Annotated Data/Hay bales 10/images'
output_dir = r'E:/BaleUAVision/Annotations Visualization/Hay bales 10/visualized_csv'

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load CSV
df = pd.read_csv(csv_file_path)

def draw_annotations_with_scaling(image_path, annotations=None, output_path=None):
    # Load the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Image not found at {image_path}.")
        return

    # Check if there are any annotations to draw
    if annotations:
        # Scaling factors based on 'magic numbers'
        width_scale = 40.56  # Adjust as needed
        height_scale = 30.4  # Adjust as needed

        for annotation in annotations:
            if 'points' in annotation:
                # Scale points
                scaled_points = [(int(x * width_scale), int(y * height_scale)) for x, y in annotation['points']]
                points = np.array(scaled_points, dtype=np.int32).reshape((-1, 1, 2))

                # Generate a random color
                color = tuple(np.random.randint(0, 255, size=3).tolist())

                # Draw transparent polygon
                overlay = image.copy()
                cv2.fillPoly(overlay, [points], color=color)
                alpha = 0.5  # Transparency factor
                cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

                # Draw bounding box
                x, y, w, h = cv2.boundingRect(points)
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

    # Save the annotated image
    if output_path:
        cv2.imwrite(output_path, image)
        print(f"Saved annotated image to: {output_path}")

# Iterate through each row of the dataframe
for index, row in df.iterrows():
    image_file_name = row['image'].split('/')[-1]  # Extract the filename from the path
    image_path = os.path.join(image_dir, image_file_name)

    if not os.path.exists(image_path):
        print(f"Image file not found: {image_path}")
        continue

    # Check if there are annotations; if 'label' is NaN, set 'annotations' to None
    if pd.isna(row['label']):
        annotations = None
    else:
        annotations = json.loads(row['label'])

    # Define the output path with "_annotated" suffix
    output_image_path = os.path.join(output_dir, image_file_name.replace('.JPG', '_annotated.JPG'))

    # Draw annotations and save the image
    draw_annotations_with_scaling(image_path, annotations, output_image_path)
