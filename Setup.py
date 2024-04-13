from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="sumfunction",
    version="0.1",
    author="Harshal Panchal",
    author_email="contact@itsmeharshal.com",
    description="A simple function to calculate the sum of two numbers.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your_username/sumfunction",
    py_modules=["sumfunction"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
