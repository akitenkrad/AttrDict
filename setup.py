"""
To install AttrDict:

    python setup.py install
"""
from setuptools import setup


DESCRIPTION = "A dict with attribute-style access"

try:
    LONG_DESCRIPTION = open('README.rst').read()
except:
    LONG_DESCRIPTION = DESCRIPTION


setup(
    name="attrdict",
    version="1.0.0",
    author="akitenkrad",
    author_email="akitenkrad@gmail.com",
    packages=("attrdict",),
    url="https://github.com/akitenkrad/attrdict",
    license="MIT License",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python :: 3",
    ] + ["Programming Language :: Python :: 3.{}".format(i) for i in range(python_min_version[1], version_range_max)]
    ,
    install_requires=(
        'six',
    ),
    tests_require=(
        'nose>=1.0',
        'coverage',
    ),
    zip_safe=True,
)
