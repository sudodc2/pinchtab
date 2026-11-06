#!/usr/bin/env python3
from pathlib import Path
from setuptools import setup, find_packages

ROOT = Path(__file__).parent
README = ROOT / "README.md"

def read_readme():
    try:
        return README.read_text(encoding="utf-8")
    except FileNotFoundError:
        return ""

setup(
    name="pinchtab",
    version="1.0.0",
    author="Hashbrown",
    author_email="299965650+sudodc2@users.noreply.github.com",
    description="Agent-native browser automation CLI for Brave and Chromium (DOMShell MCP)",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/sudodc2/pinchtab",
    project_urls={
        "Homepage": "https://github.com/sudodc2/pinchtab",
        "Issues": "https://github.com/sudodc2/pinchtab/issues",
    },
    license="Apache-2.0",
    packages=find_packages(include=["pinchtab*"]),
    python_requires=">=3.10",
    install_requires=[
        "click>=8.1,<9.0",
        "prompt-toolkit>=3.0,<4.0",
        "mcp>=0.1.0,<1.0.0",
    ],
    extras_require={"dev": ["pytest>=7", "build", "twine"]},
    entry_points={"console_scripts": ["pinchtab=pinchtab.browser_cli:main"]},
    package_data={"pinchtab": ["skills/*.md"]},
    include_package_data=True,
    zip_safe=False,
    keywords="cli browser automation mcp domshell brave ai-agent",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Internet :: WWW/HTTP :: Browsers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
)
