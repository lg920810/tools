# pip install nibabel

import nibabel as nib
import matplotlib.pyplot as plt
import numpy as np

path = '/home/legal/Datasets/LITS/test/test-volume-0.nii'

img = nib.load(path)
img_arr = img.get_fdata()
img_arr = img_arr[:,:,0].T
plt.imshow(img_arr, cmap='gray')
plt.show()
