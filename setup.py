from setuptools import find_packages,setup

HYPEN_E_DOT ='-e .'
def get_requirements(file_path: str )-> list[str]:
    from typing import List    ## this function will return a list of requirements

    requirements=[]
    with open(file_path) as file_object:
        requirements=file_object.readlines()
        requirements=[req.replace ("\n","")for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements


setup(
name='ML Project',
version='0.0.1',
author='Chinmay',
author_email='chinmay@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')   

)    