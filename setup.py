from setuptools import setup, find_packages

setup(
    name="flaskdemo",
    version="0.0.1",
    description="flaskdemo",
    author="Team",
    author_email="",
    package_dir={"": "src/"},
    packages=find_packages("src/"),
)
