from setuptools import setup, find_packages

setup(
    name="myplugin",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "tutor.plugin.v1": ["myplugin = myplugin.plugin"],
    },
    install_requires=["tutor-openedx"],
)
