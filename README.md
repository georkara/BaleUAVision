# Hay Bales Dataset - UAV Captured Imagery
# UAV Agriculture Hay Bales Dataset
# UAV-based Hay Bale Agricultural Dataset
# UAV-Captured Hay Bale Agri-Dataset
# UAV Hay Bale Field Dataset

## Description
This dataset comprises a comprehensive collection of UAV-captured images of agricultural fields with hay bales. It includes high-resolution RGB imagery, catering to a wide range of applications from precision agriculture to machine learning in computer vision and autonomous navigation.

## Dataset Details
- **Images**: High-resolution RGB images
- **Annotations**: Semantic segmentation with polygons
- **Formats**: Annotations available in COCO, CSV, JSON, YOLO formats
- **Size**: ~100GB
- **Resolution**: 4056x3040 (RGB) 
- **Flight Parameters**: Various altitudes, speeds and overlaps
- **Area Covered**: 938715 square meters (m²) in total

## Applications
- Object detection and counting (hay bales)
- Agricultural field analysis
- Training data for machine learning models in computer vision
- Simulation scenarios for unmanned ground vehicles and robotics

## Files
    ├── README.md

    ├── Hay bales Dataset
      ├── Raw Data
          ├── Hay bales 1
          ├── Hay bales 2
          ...
          └── Hay bales 16
      ├── Annotated
          ├── Hay bales 1
              ├── COCO format
              ├── CSV format
              ├── JSON format
              ├── YOLO format
              └── images
           ├── Hay bales 2
              ├── COCO format
              ├── CSV format
              ├── JSON format
              ├── YOLO format
              └── images  
           ...
           └── Hay bales 16  
              ├── COCO format
              ├── CSV format
              ├── JSON format
              ├── YOLO format
              └── images  
      ├── Orthophotos
          ├── Hay bales 1 orthophoto
          ├── Hay bales 2 orthophoto
          ...
          └── Hay bales 16 orthophoto
          
      └── Dataset Description.csv

### Files explanation
- Raw Data: Includes all UAV-captured images in raw RGB format. Note that this folder is organized/unfolded into 16 subfolders where each one represents a flight mission (one flight mission per hay bales field). Thus, each subfolder ("Hay bales 1", "Hay bale2", ... , "Hay bales 16") contains the raw RGB images for each UAV-captured field.
## Usage
The dataset is structured into folders based on the image type and annotation format. Each subfolder contains the respective images and their annotations. 

Please ensure to cite this dataset if used in your research or project.

## Citing the Dataset
To cite this dataset in your work, please use the following citation:
