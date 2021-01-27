from setuptools import setup, find_packages
from codecs import open
from os import path
import re

here = path.abspath(path.dirname(__file__))

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('cifar10/__init__.py').read(),
    re.M
    ).group(1)

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name="cifar10",
  packages=find_packages(), # this must be the same as the name above
  version=version,
  description='',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author='joeyism',
  author_email='joeyism@gmail.com',
  url='https://github.com/joeyism/cifar10', # use the URL to the github repo
  download_url='https://github.com/joeyism/cifar10/archive/{}.tar.gz'.format(version),
  keywords=['cifar', 'cifar10', 'ten', '10', 'machine', 'learning', 'database'], 
  install_requires=[package.split("\n")[0] for package in open("requirements.txt", "r").readlines()],
  classifiers=[],
  )
