from setuptools import setup, find_packages

readme = open('README.md').read()
version = open('.VERSION').read()

setup(
    name='mijnah',
    version=version,
    description='mijn albert heijn library',
    long_description=readme,
    author='F. Rejon-Barrera',
    url='https://github.com/frejonb/mijn-albert-heijn',
    packages=find_packages(exclude=('tests', 'hooks')),
    install_requires=[
        'requests==2.22.0'
    ],
    keywords='albert heijn',
)
