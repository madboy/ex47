try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'Exercise 47 from LPTHW',
        'author': 'Kristofer Lindberg',
        'url': 'https://www.github.com/madboy/ex47',
        'download_url': 'https://www.github.com/madboy/ex47',
        'author_email': 'k.lindberg@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['ex47'],
        'scripts': [],
        'name': 'Exercise47'
        }

setup(**config)
