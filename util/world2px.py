import numpy as np


def world2px(trans_mat, world_coords):
    """
    Convert SCiLS Lab world coordinates to pixel coordinates based on x-y raster points.

    :param trans_mat: 4x4 transformation matrix for a given region of interest.
    :type trans_mat: numpy.array
    :param world_coords: World coordinates for a given region of interest.
    :type world_coords: numpy.array
    :return: Tuple of x-y pixel coordinates.
    :rtype: tuple[int]
    """
    back_trans = np.linalg.inv(trans_mat)[0:2, 0:2]
    px_ind = back_trans @ world_coords
    px_ind_int = np.round(px_ind + (np.mean(np.round(px_ind) - px_ind, axis=1)[:, np.newaxis]))
    px_ind_int = px_ind_int - np.min(px_ind_int, axis=1)[:, np.newaxis] + 1
    x = px_ind_int[0, :]
    y = px_ind_int[1, :]
    return x.astype(int), y.astype(int)
