# CustomObjectDetectionUsingYolov8
 Cutom Object Detection, Segmentation and Tracking

# The dataset directory structure should look like

**data/**<br>
**├── test/**<br>
**│   ├── images/**<br>
**│   ├── labels/**<br>
**├── train/**<br>
**│   ├── images/**<br>
**│   ├── labels/**<br>
**├── valid/**<br>
**│   ├── images/**<br>
**│   ├── labels/**<br>
**└──** **data.yaml**<br>

# Split the dataset using dataset_splitter.py

# If annotations are in Pascal VOC format convert it to YOLO format using voc2yolo.py

# Use training.ipynb notebook for training