import os.path
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

README_PATH = os.path.join(HERE, 'README.rst')
try:
    README = open(README_PATH).read()
except IOError:
    README = ''

setup(
    name='ratchet',
    packages=find_packages(),
    version='0.4.1',
    entry_points= {
        'paste.filter_app_factory': [
            'pyramid=ratchet.contrib.pyramid:create_ratchet_middleware'
        ]
    },
    description='Ratchet.io generic python library',
    long_description=README,
    author='Brian Rue',
    author_email='brian@ratchet.io',
    url='http://github.com/ratchetio/pyratchet',
    classifiers=[
        "Programming Language :: Python",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Pyramid",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development",
        "Topic :: Software Development :: Bug Tracking",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Quality Assurance",
        ],
    install_requires=[
        'requests',
        ],
    )

