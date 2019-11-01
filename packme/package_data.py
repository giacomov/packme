import pkg_resources


def get_path_of_data_file(pkg_name, data_file):

    file_path = pkg_resources.resource_filename(pkg_name, 'data/%s' % data_file)

    return file_path
