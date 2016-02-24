try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
    'description': '',
    'author': 'Forrest Alvarez',
    'url': 'https://github.com/gravyboat/planet-rest-api',
    'version': '1.0',
    'install_requires': ['flask'],
    'packages': ['planet-rest-api'],
    'scripts': [],
    'name': 'planet-rest-api'
}

setup(**config)
