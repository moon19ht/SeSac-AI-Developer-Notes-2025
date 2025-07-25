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

base_path = "../../data/flowers"

print("daisy", len(os.listdir(base_path+"/daisy")))
print("dandelion", len(os.listdir(base_path+"/dandelion")))
print("sunflower", len(os.listdir(base_path+"/sunflower")))
print("rose", len(os.listdir(base_path+"/rose")))
print("tulip", len(os.listdir(base_path+"/tulip")))


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


from keras.utils import image_dataset_from_directory
from pathlib import Path

# batch_size에 지정된 만큼 폴더로부터 이미지를 읽어온다. 크기는 image_size에 지정한 값으로 가져온다.
# 훈련셋을 쪼개서 8:2 정도로 검증셋을 따로 만드는 방법도 있고, subset 속성, seed 를 이용해 나눠야 한다.
base_dir = Path(base_dir)

train_ds = image_dataset_from_directory(
    base_dir/"train",
    image_size=(180, 180),
    batch_size=16
)
validation_ds = image_dataset_from_directory(
    base_dir/"validation",
    image_size=(180, 180),
    batch_size=16
)
test_ds = image_dataset_from_directory(
    base_dir/"test",
    image_size=(180, 180),
    batch_size=16
)

# VGG19 이미지 모델 가져오기
from keras.applications.vgg19 import VGG19

def deeplearning():
    conv_base = keras.applications.vgg19.VGG19(
        weights="imagenet",
        include_top=False, # CNN만 가져와라, CNN이 하단에 있음, 상단 - 완전연결망(분류)
        input_shape=(180, 180, 3) # 입력할 데이터 크기를 주어야 한다.
        # 데이터셋에서 지정한 크기와 일치해야 한다, 3-색정보
    )

    conv_base.summary() # CNN 요약 확인하기
    # block5_pool(MaxPooling2D) (None, 5, 5, 512)

    conv_base.trainable = True
    print("합성곱 기반 층을 동결하기 전의 훈련 가능한 가중치 개수", len(conv_base.trainable_weights))
    conv_base.trainable = False # 동결
    print("합성곱 기반 층을 동결 후의 훈련 가능한 가중치 개수", len(conv_base.trainable_weights))

    data_argumentation = keras.Sequential([
        layers.RandomFlip("horizontal"),
        layers.RandomRotation(0.2),
        layers.RandomZoom(0.4)
    ])

    # 모델 만들기
    inputs = keras.Input(shape=(180, 180, 3)) # 모델의 입력레이어 정의 
    x = data_argumentation(inputs) # 입력이미지에 데이터 증강을 적용한다.
    x = keras.applications.vgg19.preprocess_input(x) # vgg19 모델에 맞는 전처리작업(픽셀값범위조정 등)

    # 인라인방식으로 cnn 연결하기
    x = conv_base(x) # 특성추출이 이뤄진다. 오래 걸린다
    #################################################
    x = layers.Flatten()(x)
    x = layers.Dense(256)(x)
    x = layers.Dense(128)(x)
    x = layers.Dense(64)(x)
    outputs = layers.Dense(5, activation="softmax")(x)

    model = keras.Model(inputs, outputs)    
    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer="adam",
                  metrics=["accuracy"])
    
    # 시스템이 내부적으로 일 처리하고 일 끝나면 우리가 전달해준 콜백함수를 호출한다.
    callbacks = [
        keras.callbacks.ModelCheckpoint(
            filepath="꽃.keras",
            save_best_only=True,
            monitor="val_loss" # 검증데이터 셋을 기준으로 하겠다 가장 적절한 시점에 호출할거다.
        )
    ]

    history = model.fit(train_ds,
                        epochs=10,
                        validation_data=validation_ds,
                        callbacks=callbacks)
    
    with open("꽃.bin", "wb") as file:
              pickle.dump(history.history, file)

deeplearning()


