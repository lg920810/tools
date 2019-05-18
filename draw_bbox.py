import pandas as pd
import numpy as np
import cv2
import os

csv = 'has_label.csv'
df3 = pd.read_csv(csv, encoding='utf-8')


pre_id = df3.iloc[0]['patientId']
image = cv2.imread(os.path.join('/home/legal/Datasets/Kaggle/train', pre_id + '.jpg'))

x, y, w, h = df3.iloc[0]['x'], df3.iloc[0]['y'], df3.iloc[0]['width'], df3.iloc[0]['height']
x, y, w, h = int(x), int(y), int(w), int(h)

for i in range(1, len(df3)):

    cur_id = df3.iloc[i]['patientId']

    if cur_id == pre_id:
        x, y, w, h = df3.iloc[i]['x'], df3.iloc[i]['y'], df3.iloc[i]['width'], df3.iloc[i]['height']
        x, y, w, h = int(x), int(y), int(w), int(h)
        cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)
    else:
        image = cv2.imread(os.path.join('/home/legal/Datasets/Kaggle/train', cur_id + '.jpg'))
        x, y, w, h = df3.iloc[i]['x'], df3.iloc[i]['y'], df3.iloc[i]['width'], df3.iloc[i]['height']
        x, y, w, h = int(x), int(y), int(w), int(h)
        cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(0, 0, 255), thickness=2)

    cv2.imwrite(os.path.join('/home/legal/Datasets/Kaggle/train_box', cur_id + '.jpg'), image)
    pre_id = cur_id
print('finished')