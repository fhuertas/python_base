import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read().strip()


required = []

setup(name='python_base',
      version=read('VERSION'),
      author="Francisco Huertas",
      author_email="pacohuertas@gmail.com",
      license="Apache2",
      packages=["package_1", "package_2"],
      description="Python base project",
      long_description=read('README.md'),
      url='https://github.com/fhuertas/python_base',
      download_url="https://github.com/fhuertas/python_base/tarball/{}".format(read('VERSION')),
      install_requires=required,
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Topic :: Utilities",
          "License :: OSI Approved :: Apache Software License",
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
      ])
