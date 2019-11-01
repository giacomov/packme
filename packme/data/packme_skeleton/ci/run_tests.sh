#!/bin/bash

##############################
# This script install the package and then run the tests against the installed version.
##############################

# Any error should cause the tests to fail
set -e

# Get the path to the directory where this script is
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Install the package
cd "${DIR}/.."
pip install .

# Run the tests against the installed version
cd "${DIR}/../tests"
pip install -r test_requirements.txt
pytest --cov={{ package_name }} -vv

# Generate coverage report
coverage html
