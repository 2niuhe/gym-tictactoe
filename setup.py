import sys
from setuptools import setup, find_packages

if sys.version_info < (3, 8):
    sys.exit('Sorry, Python < 3.8 is not supported!')

setup(name='gym_tictactoe',
      version='0.0.1',
      install_requires=['gymnasium', 'click', 'tqdm', 'pandas'],
      packages=find_packages()
      )
