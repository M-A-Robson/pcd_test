# pcd_test

Testing different methods of creating pointcloud data sets from RGBD data assuming pinhole camera model.

## Setup

* tested using Python 3.9
* installed c complier (e.g. gcc)
* clone this repo
* install python dependencies with
```
$ pip install -r requirements.txt
```
* Cython code must be complied to run (see: http://docs.cython.org/en/latest/src/quickstart/build.html), from the cloned directory run:
```
$ python setup.py build_ext --inplace
```
* run test
```
$ python top.py
```


