#!/usr/bin/env python

from os import path

from setuptools import setup

from .polyfill_callable import __doc__, __version__

project_directory = path.abspath(path.dirname(__file__))
readme_path = path.join(project_directory, 'README.rst')
library_path = path.join(project_directory, 'polyfill_callable.py')

with open(readme_path, encoding='utf-8') as readme_file:
    long_description = readme_file.read()

setup(
    name='polyfill-callable',
    version=__version__,
    description=__doc__.split('\n')[0],
    long_description=long_description,
    license='0BSD (BSD Zero Clause License)',
    url='https://github.com/mentalisttraceur/python-polyfill-callable',
    author='Alexander Kozhevnikov',
    author_email='mentalisttraceur@gmail.com',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.4',
        'Programming Language :: Python :: 2.3',
        # This probably works on older versions back through the early
        # 1.1 days, but PyPi doesn't have classifier strings for that.
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: IronPython',
        'Programming Language :: Python :: Implementation :: Jython',
        'Programming Language :: Python :: Implementation :: MicroPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: Implementation :: Stackless',
        'Operating System :: OS Independent',
    ],
    py_modules=['polyfill_callable'],
)
