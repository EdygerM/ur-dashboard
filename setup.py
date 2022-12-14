# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# To use a consistent encoding
from codecs import open
from os import path

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="ur-dashboard",
    version="0.1.0",
    description="UR Dashboard Server Communication",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://ur-dashboard.readthedocs.io/",
    author="Edy Mariano",
    author_email="edy.mariano1@gmail.com",
    license="MIT",
    classifiers=[
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        "Operating System :: OS Independent"
    ],
    packages=["ur_dashboard"],
    include_package_data=True,
    install_requires=[""]
)