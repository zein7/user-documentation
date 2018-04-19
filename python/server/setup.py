import os
from setuptools import setup, find_packages

__version__ = '0.0.1'

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='aristotle_docs_server',
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    license='',
    author='Samuel Spencer',
    author_email='sam@aristotlemetadata.com',
    zip_safe=False,
    classifiers=[
    ],
    install_requires=[
    ]

)
