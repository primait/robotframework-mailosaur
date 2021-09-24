import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="robotframework-mailosaur",
    version="0.9",
    author="Prima.it",
    author_email="",
    description="Mailosaur library for Robot framework",
    long_description=[],
    long_description_content_type="text/markdown",
    url="https://github.com/primait/robotframework-mailosaur",
    packages=['rfmailosaur'],
    install_requires=['robotframework>=4.0', 'mailosaur'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ])
