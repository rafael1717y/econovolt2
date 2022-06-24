from gettext import install

from setuptools import find_packages, setup
from sqlalchemy import desc


def read(filename):
    return [req.strip() for req in open(filename).readlines()]


setup(
    name="econovolt",
    version="1.0.0",
    description="Econovolt app",
    packages=find_packages(),
    include_package_data=True,
    install_requires=read("requirements.txt"),
    extras_require={"dev": read("requirements-dev.txt")},
)
