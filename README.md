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

## Results
* Edit top.py to change number of loops (basic python loop is excruciatingly slow)
* using AMD Ryzen 7 3700X 8-Core Processor 3.59 GHz with 32Gb Ram my results are:
```
  running 5 loops of each method to compare run times...
  running: numpy method test
  loop 0
  loop 1
  loop 2
  loop 3
  loop 4
  mean run time 0.0285 secs
  fps:35.072
  running: python_loop method test
  loop 0
  loop 1
  loop 2
  loop 3
  loop 4
  mean run time 6.5686 secs
  fps:0.152
  running: cython_loop method test
  loop 0
  loop 1
  loop 2
  loop 3
  loop 4
  mean run time 0.0127 secs
  fps:78.603
```

  Suggesting pure numpy is fast enough for a 30fps stream (and much simpler to implment) but cython achieves faster run times. Clearly further optimisations could be made and added to the test.
