import os
import re
from setuptools import setup, find_packages, find_namespace_packages

with open("cleetcode/__init__.py", "r") as f:
    data = f.read()
    _version = re.findall(r'__version__="([0-9.]+)"', data)[0]

packages = find_packages(
    where="lecode*",
    exclude=(),
    include=("*",)
)

setup(
    name="cleetcode",
    version=_version,
    description="This is a leetcode learn package",
    author="pancras",
    url="https://chenbangguo.com",
    packages=packages,
    package_data={
        "lecode": [
            "untitled.md",
            "untitled.ipynb",
        ],
    }
)

# python setup.py develop
