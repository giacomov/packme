def test_can_import_version():

    from {{ package_name }} import __version__

    assert isinstance(__version__, str)
