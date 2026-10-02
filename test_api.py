"""后端 API 接口测试示例。

使用 requests 库测试公开接口 httpbin.org（一个专门给测试用的 HTTP 服务）。
覆盖：GET / POST / 参数校验 / 状态码 / 响应字段断言。
"""
import pytest
import requests


@pytest.fixture(scope="module")
def httpbin():
    base = "https://httpbin.org"
    try:
        requests.get(base, timeout=5)
    except requests.ConnectionError:
        pytest.skip("httpbin.org 无法连接，跳过接口测试（需要联网）")
    return base


class TestGetApi:
    def test_get_returns_200(self, httpbin):
        r = requests.get(f"{httpbin}/get", timeout=10)
        assert r.status_code == 200

    def test_get_echoes_query_params(self, httpbin):
        r = requests.get(f"{httpbin}/get", params={"keyword": "test"}, timeout=10)
        assert r.json()["args"]["keyword"] == "test"

    def test_get_with_empty_param(self, httpbin):
        # 边界值：空参数
        r = requests.get(f"{httpbin}/get", params={"name": ""}, timeout=10)
        assert r.status_code == 200


class TestPostApi:
    def test_post_json_body(self, httpbin):
        payload = {"name": "lilun", "age": 20}
        r = requests.post(f"{httpbin}/post", json=payload, timeout=10)
        assert r.status_code == 200
        assert r.json()["json"] == payload

    def test_post_headers(self, httpbin):
        r = requests.post(
            f"{httpbin}/post",
            json={"a": 1},
            headers={"X-Token": "demo-token"},
            timeout=10,
        )
        assert r.status_code == 200
        assert r.json()["headers"]["X-Token"] == "demo-token"
