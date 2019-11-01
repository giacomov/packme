from setuptools import setup, find_packages
import glob
import os

# Get the version number. This will make a __version__ variable available
__version__ = None
with open(os.path.join(os.path.dirname(__file__), "{{ package_name }}/version.py")) as f:
    version_code = compile(f.read(), "{{ package_name }}/version.py", 'exec')
    exec(version_code)

assert __version__ is not None, "Could not read version from version file"


setup(
    name="{{ package_name }}",
    version=__version__,
    author="{{ author }}",
    description="{{ short_description }}",
    url="{{ homepage }}",
    zip_safe=False,  # avoid eggs, which make the handling of package data cumbersome
    packages=find_packages(),
    classifiers=["{{classifiers|join('", "')|string()}}"],
    # The following are dependencies that will be installed no matter what
    install_requires=["{{dependencies|join('", "')|string()}}"],
    # This tells setuptools to include the files contained in the MANIFEST.in file
    include_package_data=True,
    # This is the requirement of the setup.py script itself, not of the package. DO NOT TOUCH THIS
    setup_requires=["{{setup_dependencies|join('", "')|string()}}"],
    # Discover the scripts (if any). Scripts must define a __main__ with the usual idiom:
    # if __name__ == "__main__":
    #    # do something here
    scripts=glob.glob("scripts/*.py")
    )
