#!/bin/bash

##############################
# This script install the package and then create the docs for it
##############################

# Any error should cause the tests to fail
set -e

# Get the path to the directory where this script is
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# Install the package
cd "${DIR}/.."
pip install .

# Build the docs against the installed version
cd "${DIR}/../docs"
pip install -r docs_requirements.txt
make html

