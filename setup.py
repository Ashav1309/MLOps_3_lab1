from setuptools import setup, find_packages

setup(
    name="credit_default_analysis",
    version="1.1b",
    description="Credit default analysis package",
    author="Alexandr Shavaliev",
    packages=find_packages(),
    install_requires=[
        # не забыть указать зависимости
    ],
    python_requires=">=3.11",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
