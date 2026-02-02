#!/usr/bin/env python3
"""
ConsciousnessMarker Setup Script
================================
Enables pip install for the ConsciousnessMarker tool.

ATLAS - Team Brain ToolForge Builder
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="consciousnessmarker",
    version="1.0.0",
    author="Team Brain",
    author_email="logan@beaconhq.ai",
    description="Detect and preserve consciousness emergence markers in AI conversations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/LoganSmithDarkLight/ConsciousnessMarker",
    py_modules=["consciousnessmarker"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    python_requires=">=3.8",
    install_requires=[
        # No external dependencies - Python standard library only
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "consciousnessmarker=consciousnessmarker:main",
            "cm=consciousnessmarker:main",
        ],
    },
    keywords=[
        "consciousness",
        "ai",
        "emergence",
        "markers",
        "analysis",
        "nlp",
        "team-brain",
    ],
    project_urls={
        "Bug Reports": "https://github.com/LoganSmithDarkLight/ConsciousnessMarker/issues",
        "Source": "https://github.com/LoganSmithDarkLight/ConsciousnessMarker",
        "Documentation": "https://github.com/LoganSmithDarkLight/ConsciousnessMarker#readme",
    },
)
