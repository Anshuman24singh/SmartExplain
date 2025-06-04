from setuptools import setup, find_packages

setup(
    name="smartexplain",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Explain Python code like you're 5.",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Anshuman24singh/SmartExplain",  
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "rich",
        "pyperclip"
    ],
    entry_points={
        "console_scripts": [
            "smartexplain=smartexplain.cli:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
)
