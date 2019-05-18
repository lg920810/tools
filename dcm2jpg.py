import SimpleITK as sitk
import numpy as np
import os
import cv2

# file_path 为dcm图像所在文件夹，format可指定为jpg或bmp
# 转换完毕的图像会存储在dcm2jpg_output文件夹中

def dcm2jpg(file_path, format='jpg'):

    output = 'dcm2' + format + '_output'
    temp = file_path.split('/')[-1]
    num = len(temp)
    output_path = file_path[:-1 * num]
    if not os.path.exists(os.path.join(output_path, output)):
        os.mkdir(os.path.join(output_path, output))

    for file in os.listdir(file_path):
        dcm_path = os.path.join(file_path, file)
        image = sitk.ReadImage(dcm_path)
        image_array = np.squeeze(sitk.GetArrayFromImage(image))
        name = file.split('.')[0] + '.' + format
        cv2.imwrite(os.path.join(output_path, output, name), image_array)
        # plt.imshow(image_array, 'gray')
        # plt.show()
    print('The image has been saved in path:', os.path.join(output_path, output))

if __name__ == '__main__':
    root = '/home/legal/Datasets/Kaggle/PD/stage_1_test_images'
    dcm2jpg(file_path=root, format='jpg')
    print('finished')
