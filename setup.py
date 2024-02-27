from setuptools import setup, find_packages

setup(
    name="Python_Package",
    version="0.0.1",
    author="Dharmikkumar Anaghan",
    author_email="dharmikanghan1996@gmail.com",
    url="https://github.com/RekhuGopal/pythoncustompackages.git",
    description="An application that informs you of the time in different locations and timezones",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    install_requires=["click", "pytz"],
    entry_points={"console_scripts": ["Python_Package = src.main:main"]},
)