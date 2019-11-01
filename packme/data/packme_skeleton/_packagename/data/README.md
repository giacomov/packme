Place in this directory all the data files you need to access from your 
package.

These files can be found at real time by importing the 
``get_path_of_data_file`` from the ``package_data`` module that is
included by default in all packages created with ``packme``. 

For example, the path of this README.md file can be found at runtime
by doing:

```
from mypackage.package_data import get_path_of_data_file

data_path = get_path_of_data_file("README.md")
```
