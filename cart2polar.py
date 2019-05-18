import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# 先对r theta 采样, 然后再找对应原图的点插值
def cart2polar(image, N=512):
    N2 = N // 2
    output = np.zeros(image.shape, image.dtype)
    r = np.arange(start=0, stop=np.sqrt(2), step=np.sqrt(2) / N)
    t = np.arange(start=0, stop=2 * np.pi, step=2 * np.pi / N)
    R, T = np.meshgrid(r, t)
    X, Y = cv2.polarToCart(R, T, angleInDegrees=False)
    for i in range(N):
        for j in range(N):
            px = int(np.floor(N2 * X[i][j]) + N2)
            py = int(np.floor(N2 * Y[i][j]) + N2)
            if ((px >= 0 and px < N) and (py >= 0 and py < N)):
                output[i][j] = image[px][py]
    return output


def polar2cart(image, N=512):

    output = np.zeros(image.shape, image.dtype)
    x = np.arange(start=-1, stop=1, step=2.0 / N)
    y = np.arange(start=-1, stop=1, step=2.0 / N)
    X, Y = np.meshgrid(x, y)
    R, T = cv2.cartToPolar(X, Y, angleInDegrees=False)
    for i in range(N):
        for j in range(N):
            px = int(np.floor(N / (2 * np.pi) * T[i][j]))
            py = int(np.floor(N / np.sqrt(2) * R[i][j]))
            if ((px >= 0 and px < N) and (py >= 0 and py < N)):
                output[i][j] = image[px][py]
    output = output.T
    if output.shape[0] == 3:
        output = np.transpose(output, [1, 2 ,0])
    return output

def demo_mask():
    path = '/home/legal/Datasets/REFUGE/crop_train/mask/g0009.bmp'
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    image[image == 0] = 2
    image[image == 128] = 1
    image[image == 255] = 0

    plt.imshow(image, cmap='gray')
    plt.axis('off')
    plt.show()

    output = cart2polar(image)
    output[output == 1] = 128
    output[output == 2] = 255
    cv2.imwrite('g0009.bmp', output)
    plt.imshow(output, cmap='gray')
    plt.axis('off')
    plt.show()

    oo = polar2cart(output)
    plt.imshow(oo, cmap='gray')
    plt.axis('off')
    plt.show()

def demo_image():
    path = '/home/legal/Datasets/REFUGE/crop_train/image/g0009.bmp'
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    plt.imshow(image)
    plt.axis('off')
    plt.show()

    output = cart2polar(image)

    # cv2.imwrite('g0009.bmp', output)
    plt.imshow(output)
    plt.axis('off')
    plt.show()

    oo = polar2cart(output)
    plt.imshow(oo)
    plt.axis('off')
    plt.show()

if __name__ == '__main__':
    # filepath = '/home/legal/Datasets/REFUGE/crop_val/image/'
    # outputpath = '/home/legal/Datasets/REFUGE/crop_val/image_t/'
    # for i in os.listdir(filepath):
    #     file = os.path.join(filepath, i)
    #     image = cv2.imread(file)
    #     output = cart2polar(image)
    #     cv2.imwrite(os.path.join(outputpath, i), output)
    # print('finished')

    # filepath = '/home/legal/Datasets/REFUGE/crop_val/mask/'
    # outputpath = '/home/legal/Datasets/REFUGE/crop_val/mask_t/'
    # for i in os.listdir(filepath):
    #     file = os.path.join(filepath, i)
    #     image = cv2.imread(file)
    #     image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #     image[image == 0] = 2
    #     image[image == 128] = 1
    #     image[image == 255] = 0
    #     output = cart2polar(image)
    #     output[output == 1] = 128
    #     output[output == 2] = 255
    #     cv2.imwrite(os.path.join(outputpath, i), output)
    # print('finished')

    demo_image()
