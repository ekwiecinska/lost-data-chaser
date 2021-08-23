#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import io
import sys

from setuptools import setup

version = "0.0.1"

with io.open('README.md', 'r', encoding='utf-8') as readme_file:
    readme = readme_file.read()

requirements = [
    'numpy',
    'pandas',
    'scikit-learn',
    'plotly==4.1.0',
    'notebook>=5.3',
    'ipywidgets>=7.2',
    'jupyterlab==1.2.21',
    'xlrd',
    'nodejs',
]

setup(
    name='lost-data-chaser',
    version=version,
    description='Space Apps 2019 Hackathon Project for challenge "Chasers of the Lost Data"',
    long_description=readme,
    long_description_content_type='text/markdown',
    author='Emma Kwiecinska',
    author_email='ekwiecinska55@gmail.com',
    url='https://github.com/ekwiecinska/lost-data-chaser',
    packages=[
        'data_chaser',
    ],
    package_dir={'data_chaser': 'data_chaser'},
    include_package_data=True,
    python_requires='>=3.7',
    install_requires=requirements,
    license='MIT',
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
    keywords=(
        'data_chaser, lost-data-chaser, Python'
    ),
)
