from setuptools import setup, find_packages
import glob
import os

# Get the version number. This will make a __version__ variable available
__version__ = None
with open(os.path.join(os.path.dirname(__file__), "packme/version.py")) as f:
    version_code = compile(f.read(), "packme/version.py", 'exec')
    exec(version_code)

assert __version__ is not None, "Could not read version from version file"


setup(
    name="packme",
    version=__version__,
    description="Automate packaging of python code",
    url="https://github.com/giacomov/packme",
    zip_safe=False,  # avoid eggs, which make the handling of package data cumbersome
    packages=find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "Development Status :: 4 - Beta"],
    install_requires=["jinja2"],
    # This tells setuptools to include the files contained in the MANIFEST.in file
    include_package_data=True,
    # Discover the scripts (if any). Scripts must define a __main__ with the usual idiom:
    # if __name__ == "__main__":
    #    # do something here
    scripts=["scripts/packme"]
    )
