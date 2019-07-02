import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt", "r") as fh:
    requirements = fh.read().splitlines()


setuptools.setup(
    name='japana',
    version='0.2',
    author="reem-codes | Reem Ali Alghamdi",
    author_email="reem.brain@gmail.com",
    description="Japanese text analysis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/reem-codes/japana",
    packages=['japana'],
    license='MIT',
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
