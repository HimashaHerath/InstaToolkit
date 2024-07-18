from setuptools import setup, find_packages

def read(fname):
    with open(fname, encoding='utf-8') as f:
        return f.read()

setup(
    name='InstaToolkit',
    version='0.1.2',
    packages=find_packages(),
    install_requires=[
        'requests',
    ],
    python_requires='>=3.6',
    description='A versatile toolkit for automating Instagram interactions',
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    author='Himasha Herath',
    author_email='himasha626@gmail.com',
    url='https://github.com/HimashaHerath/InstaToolkit',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
