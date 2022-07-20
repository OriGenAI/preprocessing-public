from setuptools import setup, find_packages
import project


with open("requirements/prod.txt") as f:
    requirements = f.read().splitlines()


setup(
    name=project.name,
    version=project.version,
    packages=['preprocessing.modular', 'preprocessing.deck', 'preprocessing.utils'],
    install_requires=requirements,
)
