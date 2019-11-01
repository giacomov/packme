"""
Sample of package documentation
================================

This is a sample of a package documentation written in the ``__init__.py`` file of the package.

Here you should put general information as well as tutorials on how to use the package.

This document can also be accessed directly from python. If you are using ipython/jupyter, just write::

    import mypackage
    mypackage?

"""

# This import makes the following idiom possible:
# import mypackage
# print(mypackage.__version__)
from .version import __version__
