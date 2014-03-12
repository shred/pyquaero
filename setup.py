#!/usr/bin/env python

from distutils.core import setup

setup(name='pyquaero',
      version='0.1.0',
      description='Aquaero server and Python library',
      author='Richard "Shred" Körber',
      author_email='dev@shredzone.org',
      url='https://github.com/shred/aquaero',
      packages=['pyquaero'],
      install_requires=[
        'libusb >= 1.0.0',
      ],
    )
