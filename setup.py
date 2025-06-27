#!/usr/bin/env python3
"""
GPT-Rapper v2.0 Setup Script
A revolutionary AI-powered rap song generator
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="gpt-rapper",
    version="2.0.0",
    author="Ishayu Shikhare",
    author_email="ishikhar@andrew.cmu.edu",
    description="A revolutionary AI-powered rap song generator with dynamic voice selection and background beats",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Zedonkay/gpt-rapper",
    license="MIT",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Multimedia :: Sound/Audio",
        "Topic :: Artistic Software",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    entry_points={
        "console_scripts": [
            "gpt-rapper=gpt_rapper:main",
        ],
    },
    keywords="ai, rap, music, text-to-speech, openai, elevenlabs, audio, generation",
    project_urls={
        "Bug Reports": "https://github.com/Zedonkay/gpt-rapper/issues",
        "Source": "https://github.com/Zedonkay/gpt-rapper",
        "Documentation": "https://github.com/Zedonkay/gpt-rapper#readme",
    },
    include_package_data=True,
    zip_safe=False,
) 