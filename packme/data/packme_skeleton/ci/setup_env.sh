#!/bin/bash

##############################
# This script creates a virtual environment called "{{ package_name}}_testing" to be used for testing (duh)
# and creating docs
##############################

# Any error should cause the tests to fail
set -e

# First create an empty virtual environment in the home of the current user
cd ${HOME}
pip install --user virtualenv
python -m venv {{ package_name }}_testing
source {{ package_name }}_testing/bin/activate
# Upgrade to remove unnecessary warnings and get the last stuff.
pip install --upgrade pip
pip install --upgrade setuptools
