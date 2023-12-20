# Hay Bales Dataset - UAV Captured Imagery
# UAV Agriculture Hay Bales Dataset
# UAV-based Hay Bale Agricultural Dataset
# UAV-Captured Hay Bale Agri-Dataset
# UAV Hay Bale Field Dataset

## Description
This dataset comprises a comprehensive collection of UAV-captured images of agricultural fields with hay bales. It includes high-resolution RGB imagery, catering to a wide range of applications from precision agriculture to machine learning in computer vision and autonomous navigation. More specifically, it encompasses detailed UAV-captured data from agricultural fields, characterized by varied flight parameters to optimize image capture for machine learning applications. This dataset is distinctive due to its diverse altitude range (50-100m), multiple speed settings (3.7-5m/s), and different overlap ratios ensuring comprehensive field coverage. The total area covered by the dataset is 938,715 square meters, with a Ground Sampling Distance (GSD) ranging from 1.53 to 3.06 cm/pixel, facilitating fine-grained analysis. The data includes 2,599 high-resolution RGB images, each meticulously annotated for semantic segmentation, and is coupled with orthophotos to support simulation tasks such as autonomous hay bale collection scenarios. This dataset is a valuable asset for advancements in precision agriculture, offering extensive resources for developing and testing computer vision and path-planning algorithms.






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
- Raw Data: Includes all UAV-captured images in raw RGB format. Note that this folder is organized/unfolded into 16 subfolders where each one represents a flight mission (one flight mission per hay bales field). Thus, each subfolder ("Hay bales 1", "Hay bale 2", ... , "Hay bales 16") contains the raw RGB images for each UAV-captured hay field.

- Annotated:**Please note that the annotated part includes a folder named "images" where a prefix is added to the original name, like "ff4026a8-" is added to the original name "Hay_bales_1_00057". This is a standard property where adding a unique prefix ensures that each image file name is distinct, which helps in managing and referencing the images correctly in the dataset. Practically a unique prefix is added to every image for every sub-set of the annotated part in accordance with the original raw dataset.**

- Orthophotos:

- Dataset Description.csv: Contains general information and metadata. Various attributes are included to provide with additional/supportive data such as Dataset ID, Latitude and Longitude of the flight polygon, Altitude, Takeoff Speed, Flight Speed, Side and Frontal Overlap Ratios, Ground Sampling Distance (GSD), Area of Flight Polygon, Flight Time, Number of Photos in Dataset, Orthophoto availability, and the Number of Hay bales depicted. The number of hay bales are provided for the under examination field, i.e., the area of interest + the surrounding area of vision (the number of hay bales has been counted manually from the provided orthophotos).
  
## Usage
The dataset is structured into folders based on the image type and annotation format. Each subfolder contains the respective images and their annotations. 

Please ensure to cite this dataset if used in your research or project.

## Citing the Dataset
To cite this dataset in your work, please use the following citation:
