import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


requirements = [
'chirptext==0.1a18',
'Janome==0.3.9',
'lxml==4.3.4',
'mecab-python3==0.996.2',
'puchikarui==0.1a2',
'style==1.1.0',
'update==0.0.1',
]


setuptools.setup(
    name='japana',
    version='1.1',
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
