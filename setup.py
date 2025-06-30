from setuptools import setup, find_packages

setup(
    name="image_editor_pkg",
    version="1.0",
    packages=find_packages(),
    install_requires=["opencv-python>=4.5", "numpy>=1.21"],
    entry_points={"console_scripts": ["image-editor=image_editor.__main__:main"]},
)
