import numpy as np
from time import perf_counter
from fast_pcd import create_pcd_loop as c_version

def create_pcd(depth:np.ndarray, color:np.ndarray, px:float, py:float, fx:float, fy:float, max_depth:float=3000):
    rows, cols = depth.shape
    c, r = np.meshgrid(np.arange(cols), np.arange(rows), sparse=True)
    # sets invalid depth data to 0
    valid_depth = np.where((depth<max_depth)&(depth>0), depth, 0) 
    z = valid_depth
    x = valid_depth * (c - px) / fx
    y = valid_depth * (r - py) / fy
    return np.dstack((x, y, z, *np.dsplit(color,3))).reshape(-1,6)
    #[np.logical_not(pcd[:,2]==0)] # removes rows with z=0 but reduces fps from 34 --> 20!

def slow_pcd_loop(depth, color, px,py,fx,fy,max_depth=3000):
    points = []
    valid_depth = np.where((depth<max_depth)&(depth>0), depth, 0) 
    for v in range(depth.shape[1]):
        for u in range(depth.shape[0]):
            r,g,b = color[u,v,:]
            Z = valid_depth[u,v]
            if Z==0: continue
            X = (u - px) * Z / fx
            Y = (v - py) * Z / fy
            points.append([X,Y,Z,r,g,b])
    return np.asarray(points)    

if __name__ == "__main__":
    dep = np.random.random_sample((1080,720)).astype(np.float32)
    color = np.random.random_sample((1080,720,3)).astype(np.float32)
    methods = {'numpy':create_pcd, 'python_loop':slow_pcd_loop, 'cython_loop':c_version}
    print('running 5 loops of each method to compare run times...')
    for method in methods.keys():
        timer = []
        print(f'running: {method} method test')
        for i in range(5):
            print(f'loop {i}')
            start = perf_counter()
            methods[method](dep,color,1,1,1,1,3000)
            timer.append(perf_counter()-start)
        
        print(f'mean run time {np.mean(timer):.4f} secs')
        print(f'fps:{1/np.mean(timer):.3f}')