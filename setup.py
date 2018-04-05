"""
Text-file-size-checker
----

Simple script for calculating the number of lines, words and
characters in a text file

Args:
    filename: The name of the file to analyze.

Raises:
    IOError: If 'filename' does not exist or can't be read.

Returns:
    A tuple where the first element is the number of lines in
    the file, the second element is the number of words and the
    third element is the number of characters.

You can install it with
----

.. code:: bash

    $ pip install txt-file-size-checker

And run it by typing
----

.. code:: bash
    $ python3 txt-file-size-checker.py 'name_of_txt_file_to_read'

"""

from setuptools import setup

setup(name='txt-file-size-checker',
      version='0.1',
      description='Calculate the number of lines, words and characters in a text file',
      ling_description=__doc__,
      licence='MIT',
      author='Uros Jevremovic',
      author_email='jevremovic.uros91@gmail.com',
      packages=['txt-file-size-checker'],)

__author__ = 'Uros Jevremovic'