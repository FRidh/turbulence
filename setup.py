import os
import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

if os.path.exists('README.md'):
    long_description = open('README.md').read()
else:
    long_description = "A collection of classes and functions to deal with turbulence in atmospheric sound propagation."

install_requires = [
    'numpy >=1.8',
    'scipy >= 0.13',
    'matplotlib',
    'numexpr',
    ]

tests_require = [
    'pytest'
    ]

class PyTest(TestCommand):
    user_options = [('pytest-args=', 'a', "Arguments to pass to py.test")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = None

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)


setup(
    name='turbulence',
    version='0.0',
    description="A collection of classes and functions to deal with turbulence in atmospheric sound propagation.",
    long_description=long_description,
    author='Frederik Rietdijk',
    author_email='fridh@fridh.nl',
    license='LICENSE',
    packages=find_packages(exclude=["tests"]),
    scripts=[],
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
    cmdclass = {'test': PyTest},
    )
      
      
