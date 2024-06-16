# Navigate to 'dataset' directory first

# Define the dictionary
d = {
    'train': 'C:/Users/aniru/OneDrive/Desktop/CustomObjDetectionYolo/CustomObjectDetectionUsingYolov8/dataset/train/images',
    'test' : 'C:/Users/aniru/OneDrive/Desktop/CustomObjDetectionYolo/CustomObjectDetectionUsingYolov8/dataset/test/images',
    'val': 'C:/Users/aniru/OneDrive/Desktop/CustomObjDetectionYolo/CustomObjectDetectionUsingYolov8/dataset/valid/images',
    'nc': 2,
    'names': ['helmet', 'head']
}

# Write the dictionary to a YAML file with comments
with open('data.yaml', 'w') as outfile:
    outfile.write(f"train: {d['train']}\n")
    outfile.write(f"test: {d['test']}\n")
    outfile.write(f"val: {d['val']}\n\n")
    outfile.write(f"nc: {d['nc']}\n")
    outfile.write(f"names: {d['names']}\n")

print("YAML file created successfully!")