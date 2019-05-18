import Augmentor

def augmentation(image_path, mask_path, num_of_samples=10):
    # Point to a directory containing ground truth data.
    # Images with the same file names will be added as ground truth data
    # and augmented in parallel to the original data.
    p = Augmentor.Pipeline(image_path)
    p.ground_truth(mask_path)

    # Add operations to the pipeline as normal:
    # p.greyscale(probability=1)
    # p.histogram_equalisation(probability=1)
    # p.rotate(probability=1, max_left_rotation=5, max_right_rotation=5)
    p.rotate270(probability=1)
    # p.rotate180(probability=0.2)
    # p.rotate90(probability=0.2)
    # p.flip_random(probability=1)
    # p.flip_top_bottom(probability=0.2)
    # p.flip_left_right(probability=0.2)

    p.sample(num_of_samples)

if __name__ == '__main__':
    image_path = '/home/legal/Datasets/REFUGE_zip/train/image'
    mask_path = '/home/legal/Datasets/REFUGE_zip/train/mask'
    num_of_samples = 50
    augmentation(image_path, mask_path, num_of_samples)
