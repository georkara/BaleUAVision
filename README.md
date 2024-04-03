# Hay Bales Dataset - UAV Captured Imagery
# UAV Agriculture Hay Bales Dataset
# UAV-based Hay Bale Agricultural Dataset
# UAV-Captured Hay Bale Agri-Dataset
# UAV Hay Bale Field Dataset

## Description
This dataset comprises a comprehensive collection of UAV-captured images of agricultural fields with hay bales. It includes high-resolution RGB imagery (in both raw and annotated -COCO, CSV, JSON, YOLO, Segmentation Masks- formats), catering to a wide range of applications from precision agriculture to machine learning in computer vision and autonomous navigation. More specifically, it encompasses detailed UAV-captured data from agricultural fields, characterized by varied flight parameters to optimize image capture for machine learning applications. This dataset is distinctive due to its diverse altitude range (50-100m), multiple speed settings (3.7-5m/s), and different overlap ratios ensuring comprehensive field coverage. The total area covered by the dataset is 938,715 square meters, with a Ground Sampling Distance (GSD) ranging from 1.53 to 3.06 cm/pixel, facilitating fine-grained analysis. The data includes 2,599 high-resolution RGB images, each meticulously annotated for semantic segmentation, and is coupled with orthophotos to support simulation tasks such as autonomous hay bale collection scenarios. This dataset is a valuable asset for advancements in precision agriculture, offering extensive resources for developing and testing computer vision and path-planning algorithms.






## Dataset Details
- **Images**: High-resolution RGB images of 16 Hay bale fields
- **Annotations**: Semantic segmentation with polygons
- **Orthophotos**: Orthomosaic views are given for each sub-set of this dataset as a result of image stitching process
- **Formats**: Annotations available in {COCO, CSV, JSON, YOLO, Segmentation Masks} formats
- **Size**: ~43.2GB **leipoun 2 orthophotos**
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
      ├── Annotated
          ├── Hay bales 1
              ├── Hay-bales-1-YOLO  # folder which contains YOLO formated .txt files
              ├── images            # folder which contains images with prefixes
              ├── Masks             # folder that contains image segmentation masks using python script segmentation_masks.py
              ├── classes           # .txt file which contains the name of the class 
              ├── Hay-bales-1-COCO  # .json file which is for COCO format
              ├── Hay-bales-1-CSV   # classic .csv file for CSV format
              ├── Hay-bales-1-JSON  # .json file for JSON format
              └── notes
           ├── Hay bales 2
              ├── Hay-bales-2-YOLO  
              ├── images
              ├── Masks
              ├── classes           
              ├── Hay-bales-2-COCO  
              ├── Hay-bales-2-CSV  
              ├── Hay-bales-2-JSON  
              └── notes
           ...
           └── Hay bales 16  
              ├── Hay-bales-16-YOLO  
              ├── images
              ├── Masks
              ├── classes           
              ├── Hay-bales-16-COCO  
              ├── Hay-bales-16-CSV  
              ├── Hay-bales-16-JSON  
              └── notes
      ├── Orthophotos
          ├── Hay bales 1 orthophoto # .tiff images for classic orthomosaic/panorama representation
          ├── Hay bales 2 orthophoto
          ...
          └── Hay bales 16 orthophoto
      ├── Raw Data
          ├── Hay bales 1  # contains 205 .jpg images
          ├── Hay bales 2  # contains 423 .jpg images
          ...
          └── Hay bales 16 # contains 119 .jpg images    
      └── Dataset Description.csv  # contains details and metadata for each Hay bale sub-set 

### Files explanation
- Raw Data: Includes all UAV-captured images in raw RGB format. Note that this folder is organized/unfolded into 16 subfolders where each one represents a flight mission (one flight mission per hay bales field). Thus, each subfolder ("Hay bales 1", "Hay bale 2", ... , "Hay bales 16") contains the raw RGB images for each UAV-captured hay field.

- Annotated: We used the well-known open source labeling software called "Label Studio". We used the labeling process "Semantic Segmentation with Polygons" in order to have an accurate annotation so as this dataset to serve as a valuable benchmark for users that want to evaluate classic or more advanced segmentation algorithms. Also, we provide four annotation options i.e., COCO,CSV,JSON and YOLO aiming at attracting broader audience that may be intrested in individual tasks in the precision agriculture tasks or at more integrated applications within this area.

**Please note that the annotated part includes a folder named "images" where a prefix is added to the original name, like "ff4026a8-" is added to the original name "Hay_bales_1_00057". This is a standard property on how Label Studio handles the export process, where adding a unique prefix ensures that each image file name is distinct, which helps in managing and referencing the images correctly in the dataset. Practically a unique prefix is added to every image for every sub-set of the annotated part in accordance with the original raw dataset.**
 
**Note also that Label Studio often uses paths to refer to the location where the files are stored. Thus the users may notice for example path like (/data/upload/5/089c0055-Hay_bales_1_0001.JPG) in the CSV version. In this case, '089c0055-Hay_bales_1_0001.JPG' is the file name. So, the users can manipulate the strings to extract only the file names in their code in the sense of having the same file name that corresponds to the image in "images" folder excluding the path string and keeping only the filename.**

- Orthophotos: This folder includes standard orthomosaic mappings for each field case (each one of the 16 hay fields). This is the result of a classic image stitching process that encopasses all individual UAV-captured images for each hay field that is under flight examination to produce the unified representation/segmented panorama. Based on orthophotos we calculate manually the number of hay bales in the fields. These representations can be really usefull for potential users that aim to develop and evaluate algorithmic variants of the Traveling Salesman Problem in simulation scenarios for unmanned ground vehicles and robotics towards optimizing the picking process of hay bales either in individual fields or in a general area of fields. Note that many of the investigated fields are close to each other in the sense of a few dozen or max hundred meters.

- Dataset Description.csv: Contains general information and metadata. Various attributes are included to provide with additional/supportive data such as Dataset ID, Latitude and Longitude of the flight polygon, Altitude, Takeoff Speed, Flight Speed, Side and Frontal Overlap Ratios, Ground Sampling Distance (GSD), Area of Flight Polygon, Flight Time, Number of Photos in Dataset, Orthophoto availability, and the Number of Hay bales depicted. The number of hay bales are provided for the under examination field, i.e., the area of interest + the surrounding area of vision (the number of hay bales has been counted manually from the provided orthophotos).
  
## Usage
The dataset is structured into folders based on the image type and annotation format. Each subfolder contains the respective images and their annotations. 

Please ensure to cite this dataset if used in your research or project.

## Citing the Dataset
To cite this dataset in your work, please use the following citation:
