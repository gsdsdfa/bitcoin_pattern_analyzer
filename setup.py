from setuptools import setup, find_packages

setup(
    name='bpa',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'requests',
    ],
    description='A library for analyzing Bitcoin price patterns.',
    long_description=open('README.md').read(),  # Ensure you have a README.md file
    long_description_content_type='text/markdown',  # Specify the format of the long description
    author='Faiz',
    author_email='faizrb@yandex.ru',
    url='https://github.com/gsdsdfa/bitcoin_pattern_analyzer.git',  # Replace with your GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',  # Specify your license
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
    ],
    python_requires='>=3.6',  # Specify the minimum Python version
)