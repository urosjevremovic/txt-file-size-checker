"""
TextFileSizeChecker
-------------

Simple script for calculating the number of lines, words and
characters in a text file.

You can get it by downloading it directly or by typing:

    $ pip install TextFile_SizeChecker

After it is installed you can start it by simply typing in your terminal:

    $ size-checker 'name_of_txt_file_to_read'

"""


from setuptools import setup

setup(name='TextFile_SizeChecker',
      version='0.4',
      description='Calculate the number of lines, words and characters in a text file',
      long_description=__doc__,
      long_description_content_type='text/markdown',
      url="https://github.com/urosjevremovic/txt-file-size-checker",
      license='MIT',
      author='Uros Jevremovic',
      author_email='jevremovic.uros91@gmail.com',
      packages=['TextFileSizeChecker'],
      entry_points={
          "console_scripts": ["size-checker=TextFileSizeChecker.txt_file_size_checker:main"],
      },
      )

__author__ = 'Uros Jevremovic'