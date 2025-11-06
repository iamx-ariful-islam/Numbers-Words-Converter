from setuptools import setup, find_packages

setup(
    name="numbers-words-converter",
    version="1.0.0",
    packages=find_packages(),
    py_modules=["converters"],  # main module file, e.g., converters.py
    license="MIT",
    description="A simple python tool for convert numbers into words and words into numbers",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="Md. Ariful Islam",
    author_email="iamx.ariful.islam@gmail.com",
    url="https://github.com/iamx-ariful-islam/numbers-words-converter",
    project_urls={
        "Bug Tracker": "https://github.com/iamx-ariful-islam/numbers-words-converter/issues",
        "Documentation": "https://github.com/iamx-ariful-islam/numbers-words-converter#readme",
        "Source Code": "https://github.com/iamx-ariful-islam/numbers-words-converter",
    },
    install_requires=[
        # no external dependencies — keep empty if pure python
        # example if needed: "numpy >= 1.25.0"
    ],
    keywords=[
        "numbers",
        "words",
        "converter",
        "numbers-to-words",
        "words-to-numbers",
        "python",
        "text-processing",
        "utility",
        "library",
        "numbers-words-converter",
        "opensource",
        "iamx-ariful-islam",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.6",
)