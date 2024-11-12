from setuptools import find_packages ,setup
from typing import List
import os.path
from sensor.exception import SensorException
import sys
import dill
# def get_requirements()->List[str]:

#     reuirements_list : List[str] =[]

#     return reuirements_list








from setuptools import find_packages,setup
from typing import List

from sensor.exception import SensorException


def get_requirements()->List[str]:
    """


    This function will return list of requirements
    """
    requirement_list:List[str] = []

    """
    Write a code to read requirements.txt file and append each requirements in requirement_list variable.
    """
    return requirement_list




setup (

    name = "sensor",
    version = "0.0.1",
    author = "Prabhakar",
    author_email = "Prabhakarkumar313@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements(),
)


def load_object(file_path:str)->object:
    try:
        if not os.path.exists(file_path):
            raise Exception(f"The file:{file_path} is not exists")

        with open(file_path,"rb") as file_obj:
            return dill.load(file_obj)

    except Exception as e:
        raise SensorException(e,sys) from e