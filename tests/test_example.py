import pytest


class TestExample:

    @pytest.mark.parametrize("input_value,expected", [
        (1, 2),
        (2, 4),
        (3, 6),
    ])
    def test_double(self, input_value, expected, setup_function):
        result = input_value * 2
        assert result == expected, f"期望 {expected}, 实际 {result}"

    def test_string_length(self, setup_function):
        text = "Hello World"
        assert len(text) == 11

    def test_list_contains(self, setup_function):
        my_list = [1, 2, 3, 4, 5]
        assert 3 in my_list
        assert 6 not in my_list

    @pytest.mark.skip(reason="暂时跳过此测试")
    def test_skip_example(self):
        assert False

    @pytest.mark.xfail(reason="预期会失败的测试")
    def test_expected_failure(self):
        assert 1 == 2