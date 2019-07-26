from setuptools import setup, find_packages

setup(
    name="testing",
    version="0.1",
    packages=["third"]
    url="https://github.com/gitchecking/third",
    install_requires=[
        "basescript==0.3.0",
        "PyGithub==1.43.5",
    ],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
