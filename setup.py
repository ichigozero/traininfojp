from setuptools import setup, find_packages

setup(
    name='traininfojp',
    description='Yahoo! JAPAN transit page scraper modules',
    author='Gary Sentosa',
    author_email='gary.sentosa@gmail.com',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
)
