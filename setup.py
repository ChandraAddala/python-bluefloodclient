try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        #import here, cause outside the eggs aren't loaded
        import pytest
        pytest.main(self.test_args)

config = {
    'description': 'Python client for blueflood/Rackspace metrics API',
    'author': 'Chandra',
    'url': 'https://github.com/ChandraAddala/python-bluefloodclient',
    'download_url': 'https://github.com/ChandraAddala/python-bluefloodclient',
    'version': '0.1',
    'tests_require': [
        'pytest'
    ],

    'cmdclass': {'test': PyTest},

    'install_requires': [
        'requests'
    ],

    'packages': ['bluefloodclient'],
    'scripts': [],
    'name': 'python-bluefloodclient'
}

setup(**config)