# 安装依赖：pip install flask
from flask import Flask
import time
import random

app = Flask(__name__)

# 模拟一个接口
@app.route("/api/test")
def mock_api():
    # 随机延迟 50~200 毫秒，模拟真实接口
    time.sleep(random.uniform(0.05, 0.2))
    return {
        "code": 200,
        "msg": "mock接口成功",
        "data": "performance-test"
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)