from setuptools import setup, find_packages
from typing import List

PROJECT_NAME = 'Machine Learning Project'
VERSION = '0.0.1'
DESCRIPTION = 'This is machine learning project in modular coding'
AUTHOR_NAME = 'Malik Md.Asif'
EMAIL_ID = 'er.malikasif@gmail.com'

REQUIREMENTS_FILE_NAME = 'requirements.txt'
HYPEN_E_DOT = '-e .' #for install setup.py file
# step-1 requirements.txt open
# step-2 read
# step-3 \n replace '' empty


def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:  # open file
        requirement_list = requirement_file.readlines()  # read file
        requirement_list = [requirement_name.replace(
            '\n', "")for requirement_name in requirement_list]
        
        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)
        return requirement_list


setup(name=PROJECT_NAME,
      version=VERSION,
      description=DESCRIPTION,
      author=AUTHOR_NAME,
      author_email=EMAIL_ID,
      packages=find_packages(),  # find_packages go to src folder __init__.py file
      install_requires=get_requirements_list()
      )
