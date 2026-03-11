# test
""" This is a test Package"""  
from setuptools import setup, find_packages

setup(
    name="Gen-AI-Agents",
    version="0.1.0",
    packages=find_packages(exclude=("tests", "docs")),
    install_requires=[
        "langchain",
        "openai",
    ],
)
