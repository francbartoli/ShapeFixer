try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A tool to fixing inconsistencies into shapefile',
    'author': 'Francesco Bartoli',
    'url': 'https://github.com/francbartoli/ShapeFixer',
    'download_url': 'https://github.com/francbartoli/ShapeFixer/archive/master.zip',
    'author_email': 'francesco.bartoli@geobeyond.it',
    'version': '0.1',
    'packages': ['shpfixer'],
    'scripts': [],
    'name': 'ShapeFixer'
}

setup(**config)