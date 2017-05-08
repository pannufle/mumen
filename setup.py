#!/usr/bin/env python3
"""Details regarding the setup.

Details here

"""

from setuptools import setup

setup(
    name='mumen',
    description='A Python application to generate multilingual data for the MEN\
    dataset',
    author='Alexandre Kabbach',
    author_email='akabbach@gmail.com',
    # version=__import__('mumen').get_version(),
    version='0.1.0',
    url='https://github.com/akb89/mumen',
    license='MIT',
    platforms=["any"],
    packages=['mumen'],
    install_requires=['requests', 'nltk', 'pyyaml'],
    # Add test suite
    # Add entry point
)
