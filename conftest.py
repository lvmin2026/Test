import pytest


@pytest.fixture(scope="session")
def setup_session():
    print("\n=== 测试会话开始 ===")
    yield
    print("\n=== 测试会话结束 ===")


@pytest.fixture(scope="function")
def setup_function():
    print("\n--- 测试函数开始 ---")
    yield
    print("\n--- 测试函数结束 ---")