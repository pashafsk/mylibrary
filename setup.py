from setuptools import setup

setup(
    name='mylibrary',
    version='1.0.0',
    description='A description of my library',
    author='Your Name',
    author_email='your@email.com',
    packages=['mylibrary'],
    install_requires=[
        'yfinance',
        'ta',
	'datetime'
    ],
)
