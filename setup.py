import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="lambdata-han",
    version="0.0.1a",
    author="Hanchung Lee",
    author_email="lee.hanchung@gmail.com",
    description="test package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/leehanchung/lambdata-han",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
