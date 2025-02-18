import os
import cv2
from tqdm import tqdm

# Define dataset paths
dataset_path = "European Traffic Sign Dataset/"
output_path = "YOLO_dataset/"

for split in ["Training", "Testing"]:
    for class_id in range(1, 165):  # Classes are numbered 001 to 164
        class_folder = os.path.join(dataset_path, split, f"{class_id:03d}")
        output_folder = os.path.join(output_path, "images", "train" if split == "Training" else "test")

        os.makedirs(output_folder, exist_ok=True)

        if not os.path.exists(class_folder):
            continue

        for img_name in tqdm(os.listdir(class_folder)):
            if img_name.endswith(".ppm"):
                img_path = os.path.join(class_folder, img_name)
                img = cv2.imread(img_path)
                new_name = f"{class_id}_{img_name.replace('.ppm', '.jpg')}"
                cv2.imwrite(os.path.join(output_folder, new_name), img)
