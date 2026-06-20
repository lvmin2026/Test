import pytest
import json
import os


@pytest.fixture(scope="session")
def test_data_loader():
    loaded_data = {}

    def load(file_name):
        if file_name not in loaded_data:
            data_dir = os.path.join(os.path.dirname(__file__), 'test_data')
            file_path = os.path.join(data_dir, file_name)
            with open(file_path, 'r', encoding='utf-8') as f:
                loaded_data[file_name] = json.load(f)
        return loaded_data[file_name]

    return load


def pytest_generate_tests(metafunc):
    if "test_data_item" in metafunc.fixturenames:
        marker = metafunc.definition.get_closest_marker("test_data")
        if marker:
            data_file = marker.args[0]
            data_dir = os.path.join(os.path.dirname(__file__), 'test_data')
            file_path = os.path.join(data_dir, data_file)
            with open(file_path, 'r', encoding='utf-8') as f:
                test_data = json.load(f)
            
            ids = [item.get("testcase_name", f"{data_file}[{i}]") for i, item in enumerate(test_data)]
            metafunc.parametrize("test_data_item", test_data, ids=ids)