"""
Text-file-size-checker
-------------

Simple script for calculating the number of lines, words and
characters in a text file.


You can install it with
-------------

.. code:: bash

    $ pip install txt-file-size-checker

And run it by typing
-------------

.. code:: bash

    $ python3 txt-file-size-checker.py 'name_of_txt_file_to_read'
"""


from setuptools import setup

setup(name='txt-file-size-checker',
      version='1.1',
      description='Calculate the number of lines, words and characters in a text file',
      long_description=__doc__,
      url="https://github.com/urosjevremovic/txt-file-size-checker",
      licence='MIT',
      author='Uros Jevremovic',
      author_email='jevremovic.uros91@gmail.com',
      packages=['txt-file-size-checker'],)

__author__ = 'Uros Jevremovic'