import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()


required = []

setup(name='foo-bar',
      version=read('VERSION'),
      author="$author$",
      author_email="pacohuertas@gmail.com",
      license="Apache2",
      packages=['$package$'],
      package_dir={'$package$':'src/$package$'},
      description="",
      long_description=read('README.md'),
      url='https://github.com/fhuertas/python_base',
      download_url="https://github.com/fhuertas/python_base/tarball/{}".format(read('VERSION')),
      install_requires=required)
