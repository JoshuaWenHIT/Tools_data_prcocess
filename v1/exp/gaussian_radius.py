import numpy as np


def gaussian_radius(det_size, min_overlap=0.7):
    height, width = det_size

    a1 = 1
    b1 = (height + width)
    c1 = width * height * (1 - min_overlap) / (1 + min_overlap)
    sq1 = np.sqrt(b1 ** 2 - 4 * a1 * c1)
    r1 = (b1 + sq1) / 2

    a2 = 4
    b2 = 2 * (height + width)
    c2 = (1 - min_overlap) * width * height
    sq2 = np.sqrt(b2 ** 2 - 4 * a2 * c2)
    r2 = (b2 + sq2) / 2

    a3 = 4 * min_overlap
    b3 = -2 * min_overlap * (height + width)
    c3 = (min_overlap - 1) * width * height
    sq3 = np.sqrt(b3 ** 2 - 4 * a3 * c3)
    r3 = (b3 + sq3) / 2
    # return min(r1, r2, r3)
    return r1, r2, r3


def gaussian_radius_v2(det_size, min_overlap=0.7):
    height, width = det_size

    a1 = 1
    b1 = (height + width)
    c1 = width * height * (1 - min_overlap) / (1 + min_overlap)
    sq1 = np.sqrt(b1 ** 2 - 4 * a1 * c1)
    r1 = (b1 - sq1) / (2 * a1)

    a2 = 4
    b2 = 2 * (height + width)
    c2 = (1 - min_overlap) * width * height
    sq2 = np.sqrt(b2 ** 2 - 4 * a2 * c2)
    r2 = (b2 - sq2) / (2 * a2)

    a3 = 4 * min_overlap
    b3 = -2 * min_overlap * (height + width)
    c3 = (min_overlap - 1) * width * height
    sq3 = np.sqrt(b3 ** 2 - 4 * a3 * c3)
    r3 = (b3 + sq3) / (2 * a3)
    # return min(r1, r2, r3)
    return r1, r2, r3


def gaussian_radius_v3(det_size, min_overlap=0.7):
    height, width = det_size

    a = (1 + min_overlap) * (height * width) / (height ** 2 + width ** 2)
    b = -2 * (1 + min_overlap) * (height * width) / np.sqrt(height ** 2 + width ** 2)
    c = (1 - min_overlap) * height * width
    sq = np.sqrt(b ** 2 - 4 * a * c)
    r = (-b - sq) / (2 * a)
    return r


if __name__ == '__main__':
    object_size = (100, 40)
    print(gaussian_radius(object_size, min_overlap=0.7))
    print(gaussian_radius_v2(object_size, min_overlap=0.7))
    print(gaussian_radius_v3(object_size, min_overlap=0.7))
    print(gaussian_radius(object_size, min_overlap=0.8))
    print(gaussian_radius_v2(object_size, min_overlap=0.8))
    print(gaussian_radius_v3(object_size, min_overlap=0.8))
