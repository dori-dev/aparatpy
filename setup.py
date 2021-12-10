import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="aparatpy",
    version="1.0.0",
    author="Mohammad Dori",
    author_email="mr.dori.dev@gmail.com",
    description="aparat.com downloader",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dori-dev/aparatpy",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    install_requires=[
        'requests',
        'beautifulsoup4'
    ],
    python_requires=">=3.6",
)
