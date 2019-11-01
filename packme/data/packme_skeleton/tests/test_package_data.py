import pytest
import os
from {{ package_name }}.package_data import get_path_of_data_file

def test_package_data():

    # This should retrieve the README.md file which is the default content of the data directory
    path = get_path_of_data_file("README.md")

    assert os.path.exists(path)

    # Test a non existing file
    with pytest.raises(IOError):

        _ = get_path_of_data_file("i_do_not_exist", check=True)

    # If we deactivate the check, this should not raise
    _ = get_path_of_data_file("i_do_not_exist", check=False)
