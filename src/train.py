import argparse
from ultralytics import YOLO

def train_yolo(model_path, data_yaml, epochs, imgsz, exp_name):
    # Load the YOLO model
    model = YOLO(model_path)

    # Start training
    results = model.train(
        data=data_yaml,
        epochs=epochs,
        imgsz=imgsz,
        name=exp_name
    )

if __name__=='__main__':
    parser = argparse.ArgumentParser(description="YOLO training script with customizable parameters.")
    parser.add_argument('--model', type=str, default='yolo11s.pt', help='Path to the YOLO pretrained model.')
    parser.add_argument("--data", type=str, default="hay_bales.yaml", help="Path to the dataset YAML file.")
    parser.add_argument("--epochs", type=int, default=100, help="Number of epochs to train.")
    parser.add_argument("--imgsz", type=int, default=640, help="Image size.")
    parser.add_argument("--name", type=str, default="Exp", help="Experiment name.")

    args = parser.parse_args()

    train_yolo(
        model_path=args.model,
        data_yaml=args.data,
        epochs=args.epochs,
        imgsz=args.imgsz,
        exp_name=args.name
    )