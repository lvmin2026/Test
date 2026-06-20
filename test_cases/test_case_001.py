import requests
import pytest
import allure


@pytest.mark.test_data("test_data_001.json")
def test_weather_api(test_data_item, setup_function):
    testcase_name = test_data_item.get("testcase_name", "Unnamed Test")
    requests_params = test_data_item["requests_params"]
    assert_content = test_data_item["assert_content"]
    
    allure.dynamic.title(testcase_name)
    allure.dynamic.description(
        f"测试天气API\n"
        f"请求参数: {requests_params}\n"
        f"预期结果: {assert_content}"
    )

    api_url = "https://eolink.o.apispace.com/456456/weather/v001/day"
    api_token = "45ecp7iama8hbqopizgz5dhhw1v1l3sc"
    timeout = 10

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