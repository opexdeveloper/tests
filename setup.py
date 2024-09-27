from setuptools import setup, find_packages

setup(
    name="pretendapi",  
    version="0.1.4",
    author="claqz",
    author_email="opexclaqz@egmail.com",
    description="An asynchronous wrapper for the Pretend API.",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),  
    install_requires=[
        "aiohttp>=3.8.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
