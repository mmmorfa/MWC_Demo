import os
import cv2
from tqdm import tqdm

dataset_path = "European Traffic Sign Dataset/"
output_label_path = "YOLO_dataset/labels/"

os.makedirs(output_label_path + "train", exist_ok=True)
os.makedirs(output_label_path + "test", exist_ok=True)

for split in ["Training", "Testing"]:
    for class_id in range(1, 165):
        class_folder = os.path.join(dataset_path, split, f"{class_id:03d}")
        label_folder = os.path.join(output_label_path, "train" if split == "Training" else "test")

        if not os.path.exists(class_folder):
            continue

        for img_name in tqdm(os.listdir(class_folder)):
            if img_name.endswith(".ppm"):
                img_path = os.path.join(class_folder, img_name)
                img = cv2.imread(img_path)
                h, w, _ = img.shape  # Get image dimensions

                # Fake bounding box (assuming whole image is the sign)
                x_center, y_center, width, height = 0.5, 0.5, 1.0, 1.0

                # Save annotation
                annotation_name = f"{class_id}_{img_name.replace('.ppm', '.txt')}"
                with open(os.path.join(label_folder, annotation_name), "w") as f:
                    f.write(f"{class_id - 1} {x_center} {y_center} {width} {height}\n")
