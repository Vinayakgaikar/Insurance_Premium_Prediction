from setuptools import  setup , find_packages
from typing import List


#Declaring variables for setup functions
PROJECT_NAME="insurance-premium-prediction"
VERSION="0.0.3"
AUTHOR="Vinayak Gaikar"
DESCRIPTION="This is the first ineuron internship Project"
#PACKAGES=["insurance"]   # insted of this we can also use find_packeges function 
REQUIREMENT_FILEE_NAME="requirements.txt"


def get_requirements_list()->List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirenents.txt file

    return This function is going to return a list which contain name of 
    libraries mentioned in requirments.txt file

    """


    with open(REQUIREMENT_FILEE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(),
install_requires=get_requirements_list()

)


