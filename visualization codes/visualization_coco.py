import cv2
import os
import json
import numpy as np
from PIL import Image as PILImage
import random

class CocoDataset:
    def __init__(self, annotation_path, image_dir, output_dir):
        self.annotation_path = annotation_path
        self.image_dir = image_dir
        self.output_dir = output_dir
        self.colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0),
                       (255, 0, 255), (0, 255, 255)]  # List of BGR colors

        with open(self.annotation_path, 'r') as json_file:
            self.coco = json.load(json_file)

        self.process_categories()
        self.process_images()
        self.process_segmentations()

        # Ensure the output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

    def process_categories(self):
        self.categories = {}
        for category in self.coco['categories']:
            cat_id = category['id']
            self.categories[cat_id] = category

    def process_images(self):
        self.images = {}
        for image in self.coco['images']:
            image_id = image['id']
            self.images[image_id] = image

    def process_segmentations(self):
        self.segmentations = {}
        for annotation in self.coco['annotations']:
            image_id = annotation['image_id']
            if image_id not in self.segmentations:
                self.segmentations[image_id] = []
            self.segmentations[image_id].append(annotation)

    def display_image_and_save(self, image_id, output_path, show_polys=True, show_bbox=True, show_labels=True):
        if image_id not in self.images:
            print(f"Image ID {image_id} not found in the dataset.")
            return

        # Load the image
        image_info = self.images[image_id]
        image_file_name = image_info['file_name']
        image_path = os.path.join(self.image_dir, os.path.basename(image_file_name))

        if not os.path.exists(image_path):
            print(f"Image file {image_path} not found.")
            return

        image = PILImage.open(image_path).convert("RGB")
        image = np.array(image)

        # Draw segmentation polygons and bounding boxes
        for segm in self.segmentations.get(image_id, []):
            color = tuple(random.choices(range(256), k=3))  # Generate a random RGB color

            if segm['iscrowd'] == 0 and show_polys:
                for points in segm['segmentation']:
                    points = np.array(points).reshape(-1, 2).astype(np.int32)
                    cv2.polylines(image, [points], isClosed=True, color=color, thickness=2)
                    overlay = image.copy()
                    cv2.fillPoly(overlay, [points], color=color)
                    alpha = 0.5  # Transparency factor
                    cv2.addWeighted(overlay, alpha, image, 1 - alpha, 0, image)

            if show_bbox:
                bbox = segm['bbox']
                x, y, w, h = map(int, bbox)
                cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)

            if show_labels:
                label = self.categories[segm['category_id']]['name']
                x, y = int(segm['bbox'][0]), int(segm['bbox'][1])
                cv2.putText(image, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

        # Ensure the output directory exists
        os.makedirs(self.output_dir, exist_ok=True)

        # Save with '_annotated' suffix
        output_path = os.path.join(self.output_dir, os.path.basename(image_path).replace('.JPG', '_annotated.JPG'))

        # Save the annotated image
        output_image = PILImage.fromarray(image)
        output_image.save(output_path)
        print(f"Annotated image saved to {output_path}")

    def process_all_images(self):
        for image_id in self.images:
            image_info = self.images[image_id]
            output_path = os.path.join(self.output_dir, image_info['file_name'])
            self.display_image_and_save(image_id, output_path)

# Provide paths to your annotation file, image directory, and output directory
annotation_path = r'E:\BaleUAVision\Annotated Data\Hay bales 3\Hay-bales-3-COCO.json'
image_dir = r'E:\BaleUAVision\Annotated Data\Hay bales 3\images'
output_dir = r'E:\BaleUAVision\Annotations Visualization\Hay bales 3\visualized_coco'

# Create an instance of the CocoDataset class
coco_dataset = CocoDataset(annotation_path, image_dir, output_dir)

# Process all images in the directory
coco_dataset.process_all_images()
