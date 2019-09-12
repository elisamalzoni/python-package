from setuptools import setup

setup(
    name='my_hello_elisa',
    version='0.1',
    packages=['my_hello'],

    install_requires=[
        'pytest >= 5.1.1'

    ],

    scripts=['scripts/hello.py'],

    author='Elisa',
    author_email='elisa@email.com'
    )