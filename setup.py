import os
import setuptools
from setuptools import setup



setup(
    name='idresearch',
    version='0.1.2',    
    description='Welcome to idresearch package. If you want to make reading or selecting your research articles more convenient, you are in the right place.',
    url='https://github.com/nairakhils/idresearch',
    author='Adarsh Karekkat, Akhil Nair, Biswaraj Palit',
    author_email = 'adarshkarekkat@gmail.com',
    license='MIT License',
    packages=setuptools.find_packages(),
    install_requires=['requests', 'pandas', 'spacy', 
    'matplotlib',],
)
