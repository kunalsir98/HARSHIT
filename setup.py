from setuptools import setup
from typing import List

def get_requirements_list()->List[str]:
    pass


# declaring variables for setup functions 
PROJECT_NAME='housing-predictor'
VERSION='0.0.1'
AUTHOR='kunal chopde'
DESCRIPTION='THIS IS MY MACHINE LEARNING PROJECT'
PACKAGES=['housing']
REQUIREMENT_FILE_NAME='requirements.txt'

def get_requirements_list()->List[str]:
    '''
    this function is going to return a list which contain name of libraries mentioned in requirements.txt file
    '''

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_file.readlines()

setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=PACKAGES,
install_requires=get_requirements_list()
)

