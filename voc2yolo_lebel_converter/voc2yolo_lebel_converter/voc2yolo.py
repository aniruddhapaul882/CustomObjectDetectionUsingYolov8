import os
import xml.etree.ElementTree as ET

def convert_bbox(size, box):
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    x = (box[0] + box[2]) / 2.0
    y = (box[1] + box[3]) / 2.0
    w = (box[2] - box[0])
    h = (box[3] - box[1])
    x = x * dw
    y = y * dh
    w = w * dw
    h = h * dh
    return(x, y, w, h)

def convert_annotation(xml_file, lebel_path, classes):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    with open(lebel_path, 'w') as out_file:
        for obj in root.iter('object'):
            difficult = obj.find('difficult').text
            cls = obj.find('name').text
            if cls not in classes or int(difficult) == 1:
                continue
            cls_id = classes.index(cls)
            xmlbox = obj.find('bndbox')
            b = (float(xmlbox.find('xmin').text), float(xmlbox.find('ymin').text),
                 float(xmlbox.find('xmax').text), float(xmlbox.find('ymax').text))
            
            bb = convert_bbox((w, h), b)

            out_file.write(f"{cls_id} {' '.join([str(a) for a in bb])}\n")

def create_yolo_labels(xml_dir, labels_dir, classes):
    if not os.path.exists(labels_dir):
        os.makedirs(labels_dir)

    for xml_file in os.listdir(xml_dir):
        if not xml_file.endswith(".xml"):
            continue
        label_path = os.path.join(labels_dir, xml_file.replace(".xml", ".txt"))
        xml_file_path = os.path.join(xml_dir, xml_file)
        convert_annotation(xml_file_path, label_path, classes)

if __name__ == "__main__":
    # Example usage
    classes = ["helmet", "head"]

    # Path to your folder containing XML files
    xml_folder = 'VOClabels/valid'

    # Path to your folder where you want to save the YOLO labels
    output_folder = 'dataset/valid/labels'

    # Convert the annotations
    create_yolo_labels(xml_folder, output_folder, classes)