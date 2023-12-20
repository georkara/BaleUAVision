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
- **Flight Parameters**: Various altitudes and speeds
- **Area Covered**: 938715 square meters (m²)

## Applications
- Object detection and counting (hay bales)
- Agricultural field analysis
- Training data for machine learning models in computer vision
- Simulation scenarios for unmanned ground vehicles and robotics

## Files
- Chargym-Charging-Station

    ├── README.md

    ├── setup.py

    ├── Chargym_Charging_Station
      ├── envs
        ├── __init__.py
        └── Charging_Station_Enviroment.py

      ├── Files
        ├── Initial_Values.mat
        ├── Results.mat
        └── Weather.mat

      ├── images
        ├── Chargym_interaction_system.jpg
        ├── Comparison_Evaluation_Reward.png
        └── indicative_tensorboard.png

      ├── utils
        ├── Energy_Calculations.py
        ├── Init_Values.py
        ├── Simulate_Actions3.py
        └── Simulate_Station3.py

      └── __init__.py

    └── Solvers
      ├── RBC
        ├── RBC.py
        └── rbc_main.py
      ├── RL
        ├── DDPG_train.py
        └── PPO_train.py
      ├── check_env.py
      └── evaluate_trained_models.py

## Usage
The dataset is structured into folders based on the image type and annotation format. Each subfolder contains the respective images and their annotations. 

Please ensure to cite this dataset if used in your research or project.

## Citing the Dataset
To cite this dataset in your work, please use the following citation:
