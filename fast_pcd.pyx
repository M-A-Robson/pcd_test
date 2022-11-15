import numpy as np
cimport cython

from cython.parallel import prange

DTYPE = np.float32

@cython.boundscheck(False)
@cython.wraparound(False)
def create_pcd_loop(float[:, ::1] depth, float[:, :, ::1] color, float px, float py, float fx, float fy, float max_depth):
    cdef Py_ssize_t x_max = depth.shape[0]
    cdef Py_ssize_t y_max = depth.shape[1]

    result = np.zeros((x_max, y_max,6), dtype=DTYPE)
    cdef float[:, :, ::1] result_view = result

    cdef float tmp_X
    cdef float tmp_Y
    cdef Py_ssize_t u, v

    for v in prange(y_max,nogil=True):
        for u in range(x_max):
            if depth[u,v]<=0: continue
            if depth[u,v]>max_depth: continue
            tmp_X = (u - px) * depth[u,v] / fx
            tmp_Y = (v - py) * depth[u,v] / fy
            result_view[u,v,0] = tmp_X
            result_view[u,v,1] = tmp_Y
            result_view[u,v,2] = depth[u,v]
            result_view[u,v,3] = color[u,v,0]
            result_view[u,v,4] = color[u,v,1]
            result_view[u,v,0] = color[u,v,2]

    return result