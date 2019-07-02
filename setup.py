import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(

    name='japana',

    version='0.1',

    author="reem-codes | Reem Ali Alghamdi",

    author_email="reem.brain@gmail.com",

    description="Japanese text anallysis",

    long_description=long_description,

    long_description_content_type="text/markdown",

    url="https://github.com/reem-codes/japana",

    packages=setuptools.find_packages(),

    classifiers=[

        "Programming Language :: Python :: 3",

        "License :: OSI Approved :: MIT License",

        "Operating System :: OS Independent",

    ],

)