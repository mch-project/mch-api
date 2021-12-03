from setuptools import setup, find_packages


with open("requirements.txt", "r") as requirements:
    install_requires = [line for line in requirements.readlines()]

setup(
    name='mch_api',
    version='0.1.0',
    packages=find_packages(),
    install_requires=install_requires
)
