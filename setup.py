"""
TextFileSizeChecker
-------------

Simple script for calculating the number of lines, words and
characters in a text file.

You can get it by downloading it directly or by typing:

.. code:: bash

    $ pip install TextFileSizeChecker

After it is installed you can start it by simply typing in your terminal:

.. code:: bash

    $ size-checker 'name_of_txt_file_to_read'

"""


from setuptools import setup

setup(name='TextFileSizeChecker',
      version='1.0',
      description='Calculate the number of lines, words and characters in a text file',
      long_description=__doc__,
      url="https://github.com/urosjevremovic/txt-file-size-checker",
      author='Uros Jevremovic',
      author_email='jevremovic.uros91@gmail.com',
      packages=['TextFileSizeChecker'],
      entry_points={
          "console_scripts": ["size-checker=TextFileSizeChecker.txt_file_size_checker:analyze_text"],
      },
      )

__author__ = 'Uros Jevremovic'