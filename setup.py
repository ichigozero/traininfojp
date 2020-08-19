from setuptools import setup, find_packages

setup(
    name='traininfojp',
    version='1.0.0',
    description='Yahoo! JAPAN transit page scraper modules',
    license='MIT',
    author='Gary Sentosa',
    author_email='gary.sentosa@gmail.com',
    url='https://github.com/ichigozero/traininfojp',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    zip_safe=False,
    install_requires=[
        'beautifulsoup4>=4.8.2',
        'requests>=2.22.0',
    ],
)
