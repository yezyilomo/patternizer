from setuptools import setup, find_packages

setup(
    name = 'patternizer',
    version = '0.01',
    description = 'Python Library for patternizing Strings with preferred characters and fonts ',
    author = 'Yezy Ilomo',
    author_email = 'yezileliilomo@hotmail.com',
    packages = find_packages(),
    package_data = {'': ['*.ttf']},
    install_requires = ['pillow', 'numpy', 'pkg_resources'],
)
