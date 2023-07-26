from setuptools import setup, find_packages

setup(
    name='uni_eval',
    version='0.1',
    packages=['uni_eval'],
    install_requires=[
        'transformers>=4.17.0.dev0',
        'accelerate',
        'datasets>=1.8.0',
        'sentencepiece!=0.1.92',
        'protobuf',
        'rouge-score',
        'nltk',
        'py7zr',
        'torch>=1.3',
        'evaluate',
        'prettytable',
    ],
)
