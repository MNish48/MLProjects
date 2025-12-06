# using this we can install ml project as a package by running: pip install -e . and even deploy it to pypi
# simply, building our application/ml model as a package itself which we can  use in other projects for predictions.

from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->list[str]:
    """ this function will return the list of requirements """

    requirements=[]
    with open(file_path) as file_obj: # here we are opening the requirements.txt file as a file object
        requirements = file_obj.readlines() # here we are reading all the lines from the file object(requirements.txt) and storing them in the requirements list.
        requirements = [req.replace("\n","") for req in requirements] # here we are removing the new line character(\n) from each requirement in the list
        if HYPEN_E_DOT in requirements: # here we are checking if -e . is present in the requirements list
            requirements.remove(HYPEN_E_DOT) # if present we are removing it from the list 
              
    return requirements

setup(
    name="ml_project",
    version="0.0.1",
    author="Nishant",
    author_email="mendhe.nishant48@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)