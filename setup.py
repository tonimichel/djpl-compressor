#! /usr/bin/env python
import os
from setuptools import setup, find_packages

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name='djpl-compressor',
    version='0.1',
    description='Compress static files for production hosting',
    long_description=read('README.md'),
    license='The MIT License',
    keywords='django, django-productline, static files compressor',
    author='Toni Michel',
    author_email='toni.michel@schnapptack.de',
    url="https://github.com/tonimichel/djpl-compressor",
    packages=find_packages(),
    package_dir={'feature_compressor': 'feature_compressor'},
    include_package_data=True,
    scripts=[],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent'
    ],
    install_requires=[
        'django-productline',
        'django-compressor',
    ]
)
