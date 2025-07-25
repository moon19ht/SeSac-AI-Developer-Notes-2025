from keras.preprocessing import image
from keras.models import load_model 
from keras import models, layers
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np 
import random 
import PIL.Image as pilimg 
import imghdr
import pandas as pd 
import pickle 
import keras 
import os
import shutil # 디렉토리 만들기, 

def rename_images_in_class_folder(src_class_dir, class_name, dest_dir):
    os.makedirs(dest_dir, exist_ok=True)

    files = [f for f in os.listdir(src_class_dir) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    files.sort()

    for idx, fname in enumerate(files):
        src_path = os.path.join(src_class_dir, fname)
        ext = os.path.splitext(fname)[1].lower()
        new_name = f"{class_name}.{idx}{ext}"
        dst_path = os.path.join(dest_dir, new_name)
        shutil.copyfile(src_path, dst_path)

    print(f"✅ {class_name} 리네임 완료: {len(files)}개 처리됨.")
    
def rename_all_classes(original_root_dir, renamed_root_dir):
    classes = ["daisy", "dandelion", "rose", "sunflower", "tulip"]

    if os.path.exists(renamed_root_dir):
        shutil.rmtree(renamed_root_dir)
    os.makedirs(renamed_root_dir, exist_ok=True)

    for class_name in classes:
        src_class_dir = os.path.join(original_root_dir, class_name)
        rename_images_in_class_folder(src_class_dir, class_name, renamed_root_dir)
        
        
def copy_images_by_class(class_name, original_dataset_dir, dest_dirs, split_ratio=(0.5, 0.25, 0.25)):
    image_files = [
        f for f in os.listdir(original_dataset_dir)
        if f.startswith(f"{class_name}.") and f.lower().endswith(('.jpg', '.jpeg', '.png')) and os.path.isfile(os.path.join(original_dataset_dir, f))
    ]
    image_files.sort()
    random.shuffle(image_files)

    total = len(image_files)
    train_end = int(total * split_ratio[0])
    val_end = train_end + int(total * split_ratio[1])

    splits = [image_files[:train_end], image_files[train_end:val_end], image_files[val_end:]]

    for split, dst_dir in zip(splits, dest_dirs):
        os.makedirs(dst_dir, exist_ok=True)
        for fname in split:
            src = os.path.join(original_dataset_dir, fname)
            dst = os.path.join(dst_dir, fname)
            shutil.copyfile(src, dst)
            
        
def ImageCopy(renamed_dataset_dir, base_dir):
    categories = ["daisy", "dandelion", "rose", "sunflower", "tulip"]
    sets = ["train", "validation", "test"]

    if os.path.exists(base_dir):
        shutil.rmtree(base_dir)
    for set_name in sets:
        for category in categories:
            os.makedirs(os.path.join(base_dir, set_name, category), exist_ok=True)

    train_dir = os.path.join(base_dir, "train")
    val_dir = os.path.join(base_dir, "validation")
    test_dir = os.path.join(base_dir, "test")

    for category in categories:
        print(f"🔄 {category} 분할 중...")
        copy_images_by_class(
            class_name=category,
            original_dataset_dir=renamed_dataset_dir,
            dest_dirs=[
                os.path.join(train_dir, category),
                os.path.join(val_dir, category),
                os.path.join(test_dir, category)
            ],
            split_ratio=(0.5, 0.25, 0.25)
        )

    print("\n✅ 이미지 분할 복사 완료!\n")

    for set_name in sets:
        for category in categories:
            dir_path = os.path.join(base_dir, set_name, category)
            count = len(os.listdir(dir_path))
            print(f"📁 {set_name}/{category}: {count}개")
            
            
# 원본 데이터셋 폴더 (클래스별 하위 폴더 있음)
original_dataset_dir = "../../data/flowers"

# 리네임된 이미지들이 저장될 위치
renamed_root = "../../data/flowers_renamed"

# 최종 분할된 train/val/test 폴더 생성 위치
base_dir = "../../data/flowers_small"

# 1단계: 클래스별 이미지들을 daisy.0.jpg 형식으로 리네임 + 통합
rename_all_classes(original_dataset_dir, renamed_root)

# 2단계: 리네임된 이미지를 2:1:1 비율로 train/validation/test 분할 복사
ImageCopy(renamed_root, base_dir)

def deeplearning():
    data_augmentation = keras.Sequential([
        layers.RandomFlip("horizontal", input_shape=(180, 180, 3)),
        layers.RandomRotation(0.1),
        layers.RandomZoom(0.1),
    ])

    model = models.Sequential()
    model.add(layers.Rescaling(1./255))
    model.add(data_augmentation)
    model.add(layers.Conv2D(32, (3, 3), activation="relu"))
    model.add(layers.MaxPooling2D(2, 2))
    model.add(layers.Conv2D(64, (3, 3), activation="relu"))
    model.add(layers.MaxPooling2D(2, 2))
    model.add(layers.Conv2D(32, (3, 3), activation="relu"))
    model.add(layers.MaxPooling2D(2, 2))
    model.add(layers.Flatten())
    model.add(layers.Dropout(0.5))
    model.add(layers.Dense(128, activation="relu"))
    model.add(layers.Dense(64, activation="relu"))
    model.add(layers.Dense(5, activation="softmax"))  # 👈 클래스 수 = 5

    model.compile(
        optimizer="adam",
        loss="sparse_categorical_crossentropy",        # 👈 정수 라벨용 다중 분류
        metrics=["accuracy"]
    )

    train_ds = keras.utils.image_dataset_from_directory(
        train_dir,
        validation_split=0.2,
        seed=123,
        subset="training",
        image_size=(180, 180),
        batch_size=16
    )

    validation_ds = keras.utils.image_dataset_from_directory(
        validation_dir,
        validation_split=0.2,
        seed=123,
        subset="validation",
        image_size=(180, 180),
        batch_size=16
    )

    model.fit(train_ds, 
              validation_data=validation_ds,
              epochs=30)

    model.save("flowers_model.keras")

deeplearning()
