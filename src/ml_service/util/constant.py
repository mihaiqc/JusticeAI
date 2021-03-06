import os


class Path:
    """
    Super annoying relative imports done here
    """
    root_directory = os.path.abspath(__file__ + "r/../../")

    __rel_path = r'data/raw/text_bk/'
    raw_data_directory = os.path.join(root_directory, __rel_path)

    __rel_path = r'data/binary/'
    binary_directory = os.path.join(root_directory, __rel_path)

    __rel_path = r'data/cluster/'
    cluster_directory = os.path.join(root_directory, __rel_path)

    __rel_path = r'data/cache/'
    cache_directory = os.path.join(root_directory, __rel_path)

    __rel_path = r'data/test/'
    test_directory = os.path.join(root_directory, __rel_path)

    __rel_path = r'data/test/mock_precedent/'
    test_mock_precedent_directory = os.path.join(root_directory, __rel_path)

    __rel_path = r'data/test/regex/'
    test_regex_directory = os.path.join(root_directory, __rel_path)
