#!/usr/bin/env bash
export DEVELOP_PYTHON_VERSION=$pythonVersion$
export TEST_PYTHON_VERSION=($pythonVersion$)

export TEST_VERBOSITY=3

export PACKAGES=("src/$package$")
export TEST_FOLDERS=("tests/$package$")
