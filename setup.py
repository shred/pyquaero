#
# pyquaero - a Python library for Aquaero fan controllers
#
# Copyright (C) 2018 Richard "Shred" Körber
#   https://github.com/shred/pyquaero
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='pyquaero',
    version='1.0.1',
    description='Library and server for Aquaero cooler controllers',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/shred/pyquaero',
    keywords='library server aquaero cooling usb',
    license='GPLv3+',

    python_requires='>=3',

    author='Richard Körber',
    author_email='dev@shredzone.de',

    project_urls={
        'Documentation': 'https://shredzone.org/docs/pyquaero/index.html',
        'Source': 'https://github.com/shred/pyquaero',
        'Tracker': 'https://github.com/shred/pyquaero/issues',
    },

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries',
        'Topic :: System :: Hardware :: Hardware Drivers',
        'Topic :: System :: Monitoring',
        'Topic :: Utilities',
    ],

    packages=['pyquaero', 'pyquaero.struct', 'pyqtools'],
    install_requires=[
        'pyusb >= 1.0.0',
    ],

    entry_points={
        'console_scripts': [
            'pyqd=pyqtools.pyqd:main',
            'pyqsettime=pyqtools.pyqsettime:main',
        ],
    },
)
