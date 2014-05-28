import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
setup(
    name = "NeuroPi",
    version = "0.1.0",
    author = "Valerie Magri",
    author_email = "valerie.magri@gmail.com",
    description = ("An experiment in reading data from a NeuroSky Mindwave into a Raspberry Pi."),
    license = "GNU GPL 3.0",
    keywords = "bci raspberrypi neurosky",
    url = "https://github.com/ArcticSphinx/NeuroPi",
    packages=['neuropi'],
    long_description=read('README.md'),
    classifiers=["Development Status :: 3 - Alpha"],
)
