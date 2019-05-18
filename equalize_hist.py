import cv2
from skimage import io
import os

#
def equalize_hist(src_dir, dst_dir):
    for root, dirc, files in os.walk(src_dir):
        for i, file in enumerate(files):
            if file.endswith('.jpg'):
                print(i)
                image = io.imread(file_path + file)
                eqImage = cv2.equalizeHist(image)
                io.imsave(dst_dir + file, eqImage)

file_path = '/data/legal/Datasets/LUNG/'
out_path = '/data/legal/Datasets/LUNG-hist/'

