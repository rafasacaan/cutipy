from setuptools import setup, find_packages

setup(
    name='cutipy',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'matplotlib',
    ],
    description='A package to apply custom styles to matplotlib plots',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Rafael Sacaan A.',
    author_email='rafasacaan@gmail.com',
    url='https://github.com/rafasacaan/cutipy', 
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
