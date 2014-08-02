#!/user/bin/env python
""" axosoft_api Module. """
from setuptools import setup, find_packages

setup(
    name="axosoft_api",
    version="0.1.0",
    description="An Axosoft API Client",
    license="MIT",
    install_requires=["requests", "six", "json"],
    author="Clifton Kaznocha",
    author_email="clifton@kaznocha.com",
    url="http://github.com/ckaznocha/axosoft-python",
    packages=find_packages(),
    keywords="Axosoft"
)
