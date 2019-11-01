import pkg_resources
import os


def get_path_of_data_file(data_file, check=False):
    """
    Returns the path of the data file as it is installed. That path can be used to read the file from the user
    installation.

    :param data_file: path of data file relative to the ``data`` directory in the main package
    :param check: check whether the file truly exists at the returned path. Default: True. If there was a problem at
           installation time and the required file was not installed, this might fail.
    :return: path of data file
    """

    file_path = pkg_resources.resource_filename("{{ package_name }}", 'data/%s' % data_file)

    if check:

        if not os.path.exists(file_path):

            raise IOError(f"Package data file {data_file} is not installed as {file_path}")

    return file_path
