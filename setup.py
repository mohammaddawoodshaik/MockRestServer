from setuptools import setup, find_packages
import os


def get_install_requirements():
    """ get install requirements from requirements.txt """
    with open('requirements.txt') as f:
        requirements = f.read().splitlines()
    return requirements


package_version = os.getenv("PACKAGE_VERSION", "0.1")
install_requires = get_install_requirements()


setup(
    name="mockrestserver",
    version=package_version,
    packages=["mockrestserver"],
    package_data={
        "": ["*.yml", "*.json", "*.crt", "*.key"]
    },
    install_requires=install_requires,
    dependency_links=[],
    url="",
    description="mockrestserver - Code-less (%s)" % package_version,
    long_description=open("README.md").read()
)
