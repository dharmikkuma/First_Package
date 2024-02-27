from setuptools import setup, find_packages
from typing import List
from pathlib import Path


HYPEN_E_DOT = "-e ."
def get_requirements(file_path:str)-> List[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements


with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="Pyt_ca", # name of your Pipy package
    version="0.0.2",
    author="Dharmikkumar Anaghan",
    author_email="dharmikanghan1996@gmail.com",
    url="https://github.com/dharmikkuma/First_Package.git",
    description="An application that informs you of the time in different locations and timezones",
    long_description=long_description,
    long_description_content="text/markdown",
    install_requires= ["numpy","flake8", "pytest","tox","mypy>=0.971","black>=22.8.0","tox-gh-actions","pathlib"],
    package_dir = {"": "src"},
    packages=find_packages(where = "src"),
    )