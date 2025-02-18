import shutil
import random
import os

dataset_path = "YOLO_dataset/images/"
train_path = "YOLO_dataset/images/train/"
val_path = "YOLO_dataset/images/val/"

os.makedirs(val_path, exist_ok=True)

all_images = os.listdir(train_path)
random.shuffle(all_images)

val_split = int(len(all_images) * 0.1)  # 10% for validation

for img in all_images[:val_split]:
    shutil.move(os.path.join(train_path, img), os.path.join(val_path, img))
