from slip_detector_both import slip_detector
import matplotlib.pyplot as plt
import cv2, os, glob
import numpy as np
import re
from tqdm import tqdm

def numericalSort(value):
    numbers = re.compile(r'(\d+)')
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

data_dir = '/home/sangwoon/github/data/openpush/'
for d in os.listdir(data_dir):
    print(f'working on {d}')
    for dd in tqdm(os.listdir(data_dir+d)):
        imgs_1 = sorted(glob.glob(f'{data_dir}{d}/{dd}/g1_*.jpg'), key=numericalSort)
        imgs_2 = sorted(glob.glob(f'{data_dir}{d}/{dd}/g2_*.jpg'), key=numericalSort)
        sd = slip_detector()
        for i in range(len(imgs_1)):
            img_1, x_1, y_1, u_1, v_1 = sd.call_back1(cv2.imread(imgs_1[i]))
            img_2, x_2, y_2, u_2, v_2 = sd.call_back2(cv2.imread(imgs_2[i]))
            for j in range(len(x_1)):
                img_1 = cv2.circle(img_1, (int(x_1[j]),int(y_1[j])), radius=0, color=(0, 0, 255), thickness=5)
            for j in range(len(x_2)):
                img_2 = cv2.circle(img_2, (int(x_2[j]),int(y_2[j])), radius=0, color=(0, 0, 255), thickness=5)
            cv2.imwrite(f'{data_dir}{d}/{dd}/markers_g1_{i}.jpg', img_1)
            np.save(f'{data_dir}{d}/{dd}/xyuv_g1_{i}.npy',np.vstack((x_1,y_1,u_1,v_1)).T)
            cv2.imwrite(f'{data_dir}{d}/{dd}/markers_g2_{i}.jpg', img_2)
            np.save(f'{data_dir}{d}/{dd}/xyuv_g2_{i}.npy',np.vstack((x_2,y_2,u_2,v_2)).T)