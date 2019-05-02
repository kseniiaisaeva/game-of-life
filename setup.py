from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
        name='gameoflife',
        version='0.0.1',
        description='Example Python Project',
        long_description=readme,
        author='John Joe',
        author_email='johndoe@example.com',
        url='https://github.com/johndoe/gameoflife-py',
        license=license,
        packages=find_packages(exclude=('tests'))
        )

