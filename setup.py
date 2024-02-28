from setuptools import setup, find_packages
from typing import List
from pathlib import Path

with open('README.md') as f:
    long_description = f.read()

setup(
    name="pyt_calc", # name of your Pipy package
    version="0.0.1",
    author="Dharmikkumar Anaghan",
    author_email="dharmikanghan1996@gmail.com",
    url="https://github.com/dharmikkuma/First_Package.git",
    description="An application that calculates",
    long_description=str(long_description),
    long_description_content="text/markdown",
    requires= ["numpy"],
    package_dir = {"": "src"},
    packages=find_packages(where = "src"),
    )