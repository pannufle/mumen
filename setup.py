#!/usr/bin/env python3
"""MuMEN setup."""

from setuptools import setup

setup(
    name='mumen',
    description='A Python application to generate multilingual data for the MEN\
    dataset',
    author='Alexandre Kabbach',
    author_email='akb@3azouz.net',
    version='0.1.0',
    url='https://github.com/akb89/mumen',
    license='MIT',
    platforms=['any'],
    packages=['mumen'],
    entry_points={
        'console_scripts': [
            'mumen = mumen.main:main'
        ],
    },
    install_requires=['requests==2.13.0', 'nltk==3.2.5', 'PyYAML==3.12',
                      'lxml==4.1.1'],
    setup_requires=['pytest-runner==4.0', 'pytest-pylint==0.8.0'],
    tests_require=['pytest==3.4.1', 'pylint==1.8.2', 'pytest-cov==2.5.1',
                   'pycodestyle==2.3.1', 'pydocstyle==2.1.1'],
    classifiers=['Development Status :: 2 - Pre-Alpha',
                 'Intended Audience :: Developers',
                 'Intended Audience :: Education',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: MIT License',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 3.5',
                 'Programming Language :: Python :: 3.6',
                 'Topic :: Scientific/Engineering :: Artificial Intelligence',
                 'Topic :: Software Development :: Libraries :: Python Modules',
                 'Topic :: Text Processing :: Linguistic'],
    zip_safe=True,
)
