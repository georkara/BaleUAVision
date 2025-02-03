# BaleUAVision: Hay Bales UAV Captured Dataset
![BaleUAVision Logo](BaleUAVision%20logo.png)

## Description
This dataset comprises a comprehensive collection of UAV-captured images of agricultural fields with hay bales. It includes high-resolution RGB imagery (in both raw and annotated -COCO, CSV, JSON, YOLO, Segmentation Masks- formats), catering to a wide range of applications from precision agriculture to machine learning in computer vision and autonomous navigation. More specifically, it encompasses detailed UAV-captured data from agricultural fields, characterized by varied flight parameters to optimize image capture for machine learning applications. This dataset is distinctive due to its diverse altitude range (50-100m), multiple speed settings (3.7-5m/s), and different overlap ratios ensuring comprehensive field coverage. The total area covered by the dataset is 938,715 square meters, with a Ground Sampling Distance (GSD) ranging from 1.53 to 3.06 cm/pixel, facilitating fine-grained analysis. The data includes 2,599 high-resolution RGB images, each meticulously annotated for semantic segmentation, and is coupled with orthophotos to support simulation tasks such as autonomous hay bale collection scenarios. This dataset is a valuable asset for advancements in precision agriculture, offering extensive resources for developing and testing computer vision and path-planning algorithms.

## Dataset Details
- **Images**: High-resolution RGB images of 16 Hay bale fields
- **Number of images**: 2,599
- **Formats**: Raw RGB images and Annotated images in {COCO, CSV, JSON, YOLO, Segmentation Masks} formats
- **Annotations**: Semantic segmentation with polygons
- **Annotation Software Used**: Label Studio
- **Captured Fields**: The dataset includes imagery from 16 fields, with 14 located in the Xanthi region and 2 in the Drama region, both situated in the northern part of Greece
- **Orthophotos**: Orthomosaic views for each subset of the dataset, generated through an image stitching process, offering a macro-perspective of the fields
- **Size**: ~44GB 
- **Resolution**: 4056x3040 (RGB) 
- **Flight Parameters**: Various altitudes, speeds and overlaps
- **Total Area Covered**: 938,715 square meters (m²) in total
- **Additional Information**: The number of hay bales has been manually counted for each field, providing a reliable reference for users aiming to develop or evaluate algorithms for automated hay bale counting

## Dataset Details Table

| Attribute            | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| **Images**           | High-resolution RGB images of 16 hay bale fields                          |
| **Number of Images** | 2,599                                                                     |
| **Formats**          | Raw RGB images and annotated images in {COCO, CSV, JSON, YOLO, Segmentation Masks} formats |
| **Annotations**      | Semantic segmentation with polygons                                       |
| **Annotation Software Used**      | Label Studio                                       |
| **Captured Fields**  | Imagery from 16 fields, with 14 located in the Xanthi region and 2 in the Drama region, both situated in the northern part of Greece |
| **Orthophotos**      | Orthomosaic views for each subset of the dataset, generated through an image stitching process, offering a macro-perspective of the fields          |
| **Size**             | ~44GB                                                                     |
| **Resolution**       | 4056 x 3040 (RGB)                                                         |
| **Flight Parameters**| Various altitudes, speeds, and overlaps                                   |
| **Total Area Covered**| 938,715 square meters (m²)                                                |
| **Additional Info**  | The number of hay bales has been manually counted for each field, providing a reliable reference for users aiming to develop or evaluate algorithms for automated hay bale counting      |

## General Information and Metadata
| Dataset ID   | Altitude (m) | Takeoff Speed (m/s) | Speed (m/s) | Side Overlap (%) | Frontal Overlap (%) | GSD (cm/pixel) | Area (m²) | Flight Time | Photos | Hay Bale Count         |
|--------------|--------------|---------------------|-------------|------------------|---------------------|----------------|-----------|-------------|--------|------------------------|
| hay bales 1  | 50           | 10                  | 3.7         | 70               | 80                  | 1.53           | 22,339    | 9 m 3 s     | 205    | 41 + 0                |
| hay bales 2  | 50           | 10                  | 3.7         | 70               | 80                  | 1.53           | 59,796    | 18 m 34 s   | 423    | -                      |
| hay bales 3  | 50           | 10                  | 3.7         | 70               | 80                  | 1.53           | 7,718     | 3 m 55 s    | 86     | 17 + 0                |
| hay bales 4  | 100          | 10                  | 5.0         | 70               | 80                  | 3.06           | 166,778   | 19 m 30 s   | 286    | -                      |
| hay bales 5  | 50           | 10                  | 3.7         | 70               | 80                  | 1.53           | 47,865    | 15 m 23 s   | 346    | -                      |
| hay bales 6  | 50           | 10                  | 3.7         | 70               | 80                  | 1.53           | 21,367    | 8 m 22 s    | 188    | -                      |
| hay bales 7  | 100          | 10                  | 5.0         | 70               | 80                  | 3.06           | 68,327    | 10 m 24 s   | 165    | -                      |
| hay bales 8  | 50           | 10                  | 3.7         | 60               | 70                  | 1.53           | 24,376    | 6 m 31 s    | 103    | -                      |
| hay bales 9  | 100          | 10                  | 5.0         | 70               | 80                  | 3.06           | 67,371    | 9 m 17 s    | 145    | -                      |
| hay bales 10 | 100          | 10                  | 5.0         | 70               | 80                  | 3.06           | 25,423    | 3 m 40 s    | 61     | 31 + 12               |
| hay bales 11 | 100          | 10                  | 5.0         | 70               | 80                  | 3.06           | 79,038    | 10 m 52 s   | 172    | -                      |
| hay bales 12 | 100          | 10                  | 5.0         | 70               | 55                  | 3.06           | 80,005    | 11 m 7 s    | 80     | -                      |
| hay bales 13 | 100          | 10                  | 5.0         | 60               | 65                  | 3.06           | 33,296    | 4 m 7 s     | 40     | 83 + 0                |
| hay bales 14 | 100          | 10                  | 5.0         | 65               | 70                  | 3.06           | 30,462    | 4 m 20 s    | 47     | 54 + 9                |
| hay bales 15 | 100          | 10                  | 5.0         | 60               | 65                  | 3.06           | 140,991   | 14 m 25 s   | 133    | 40 check again         |
| hay bales 16 | 80           | 10                  | 5.0         | 60               | 70                  | 2.45           | 63,563    | 8 m 59 s    | 119    | -                      |


## Applications

The **UAV-Captured Hay Bale Dataset** can serve as a valuable resource in a variety of fields, including but not limited to:

- **Object Detection and Counting**: Automating the detection and counting of hay bales in agricultural fields.
- **Agricultural Field Analysis**: Supporting precision agriculture by analyzing field conditions and optimizing resource allocation.
- **Training Data for Machine Learning Models**: Providing a benchmark dataset for developing and testing computer vision algorithms.
- **Simulation Scenarios for Robotics**: Enabling the design and evaluation of autonomous systems for unmanned ground vehicles, focusing on tasks such as hay bale collection.


## Files
    ├── README.md
    ├── Hay bales Dataset
      ├── Annotated
          ├── Hay bales 1
              ├── Hay-bales-1-YOLO  # folder which contains **YOLO** formated .txt files
              ├── images            # folder which contains images with prefixes
              ├── Masks             # folder that contains image **Segmentation Masks** using the python script "segmentation_masks.py"
              ├── classes           # .txt file which contains the name of the class 
              ├── Hay-bales-1-COCO  # .json file which is for **COCO** format
              ├── Hay-bales-1-CSV   # classic .csv file for **CSV** format
              ├── Hay-bales-1-JSON  # .json file for **JSON** format
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

**Please note that the annotated part includes a folder named "images" where a prefix is added to the original name of each image, like "ff4026a8-" is added to the original name "Hay_bales_1_00057". This is a standard property on how Label Studio handles the export process, where adding a unique prefix ensures that each image file name is distinct, which helps in managing and referencing the images correctly in the dataset. Practically a unique prefix is added to every image for every sub-set of the annotated part in accordance with the original raw dataset.**
 
**Note also that Label Studio often uses paths to refer to the location where the files are stored. Thus the users may notice for example path like (/data/upload/5/089c0055-Hay_bales_1_0001.JPG) in the CSV version. In this case, '089c0055-Hay_bales_1_0001.JPG' is the file name. So, the users can manipulate the strings to extract only the file names in their code in the sense of having the same file name that corresponds to the image in "images" folder excluding the path string and keeping only the filename.**

- Orthophotos: This folder includes standard orthomosaic mappings for each field case (each one of the 16 hay fields). This is the result of a classic image stitching process that encopasses all individual UAV-captured images for each hay field that is under flight examination to produce the unified representation/segmented panorama. Based on orthophotos we calculate manually the number of hay bales in the fields. These representations can be really usefull for potential users that aim to develop and evaluate algorithmic variants of the Traveling Salesman Problem in simulation scenarios for unmanned ground vehicles and robotics towards optimizing the picking process of hay bales either in individual fields or in a general area of fields. Note that many of the investigated fields are close to each other in the sense of a few dozen or max hundred meters.

- Dataset Description.csv: Contains general information and metadata. Various attributes are included to provide with additional/supportive data such as Dataset ID, Latitude and Longitude of the flight polygon, Altitude, Takeoff Speed, Flight Speed, Side and Frontal Overlap Ratios, Ground Sampling Distance (GSD), Area of Flight Polygon, Flight Time, Number of Photos in Dataset, Orthophoto availability, and the Number of Hay bales depicted. The number of hay bales are provided for the under examination field, i.e., the area of interest + the surrounding area of vision (the number of hay bales has been counted manually from the provided orthophotos).

### Visualize Annotations
In case that you want to inspect the annotated images, we offer options through the python scripts: visualization_json.py; visualization_csv.py; visualization_coco.py; visualization_coco2.py;
  
## Usage
The dataset is structured into folders based on the image type and annotation format. Each subfolder contains the respective images and their annotations. 

Please ensure to cite this dataset if used in your research or project.

## Citing the Dataset
To cite this dataset in your work, please use the following citation:
