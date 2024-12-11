import os
import sys
from setuptools import setup, find_packages

# Read requirements
def read_requirements(filename):
    with open(filename) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Read README
def read_readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='avion',
    version='1.0.0',
    description='Advanced AI-Powered Token Generation Framework',
    long_description=read_readme(),
    long_description_content_type='text/markdown',
    author='AVION Team',
    author_email='dev@avion.ai',
    url='https://github.com/yourusername/avion',
    packages=find_packages(),
    install_requires=read_requirements('requirements.txt'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires='>=3.8',
) 