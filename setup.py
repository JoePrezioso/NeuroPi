from distutils.core import setup

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
    long_description=read('README'),
    classifiers=[],
)
