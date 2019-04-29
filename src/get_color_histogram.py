import numpy as np


def get_color_histogram(image, superpixels, index):
    indices = np.where(superpixels.ravel() == index)[0]
    r_hist = np.bincount(image[:, :, 0].ravel()[indices], minlength=256)
    g_hist = np.bincount(image[:, :, 1].ravel()[indices], minlength=256)
    b_hist = np.bincount(image[:, :, 2].ravel()[indices], minlength=256)

    histogram = (r_hist + g_hist + b_hist) / 3
    return histogram
