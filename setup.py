import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gthb",
    version="0.0.1",
    author="Hannan Satopay",
    author_email="sathannan@hotmail.com",
    description="A library for everything Github",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="Apache 2.0",
    url="https://github.com/hannansatopay/gthb",
    packages=setuptools.find_packages(),
    install_requires=['requests'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
