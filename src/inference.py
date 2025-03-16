from ultralytics import YOLO
import glob
import os
from natsort import natsorted


def run_inference(model_path, image_dir, output_dir):
    # Load YOLO model
    model = YOLO(model_path)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Collect and sort image paths
    imgs = glob.glob(os.path.join(image_dir, "*.JPG"))
    sorted_paths = sorted(imgs, key=lambda x: int(os.path.splitext(x.split('_')[-1])[0]))

    # Run inference
    results = model(sorted_paths)

    # Save results retaining original filenames
    for img_path, result in zip(sorted_paths, results):
        filename = os.path.basename(img_path)  # Retain original filename
        result.save(filename=os.path.join(output_dir, filename))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Run YOLO inference on a directory of images.")
    parser.add_argument('--model', type=str, default="weights/location_split.pt",
                        help='Path to the trained YOLO model.')
    parser.add_argument('--image_dir', type=str, default="data/Hay bales 15/images",
                        help='Path to the directory containing images.')
    parser.add_argument('--output_dir', type=str, default="HB_infer", help='Directory to save inference results.')

    args = parser.parse_args()

    run_inference(args.model, args.image_dir, args.output_dir)
