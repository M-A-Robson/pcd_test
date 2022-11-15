from setuptools import setup
from Cython.Build import cythonize

setup(
    name='fast_pcd',
    ext_modules=cythonize('fast_pcd.pyx'),
    zip_safe=False,
)