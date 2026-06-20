import requests
import pytest


@pytest.mark.test_data("test_data_002.json")
def test_weather_api_v2(test_data_item, setup_function):
    api_url = "https://eolink.o.apispace.com/456456/weather/v001/day"
    api_token = "45ecp7iama8hbqopizgz5dhhw1v1l3sc"
    timeout = 10

    requests_params = test_data_item["requests_params"]
    assert_content = test_data_item["assert_content"]

    headers = {"X-APISpace-Token": api_token}
    response = requests.get(
        api_url,
        params=requests_params,
        headers=headers,
        timeout=timeout,
    )
    data = response.json()
    actual_value = data['result']['location']['name']

    assert actual_value == assert_content, f"期望 {assert_content}, 实际 {actual_value}"
    print(f"测试通过: {actual_value} == {assert_content}")