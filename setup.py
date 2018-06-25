"""
Good Handlers

Method and function handlers that implement common
behaviors without writing the entire function

Author:  Anshul Kharbanda
Created: 6 - 24 - 2018
"""
from setuptools import setup

# Read README.md
with open('README.md', 'r') as file:
    readme_text = file.read()

# Create setup function
setup(name='good-handlers',
      version='1.0.1',
      description='Method and function handlers that implement common behavior',
      long_description=readme_text,
      long_description_content_type='text/markdown',
      author='Anshul Kharbanda',
      author_email='akanshul97@gmail.com',
      url='https://www.github.org/andydevs/good-handlers',
      packages=['good_handlers'])
