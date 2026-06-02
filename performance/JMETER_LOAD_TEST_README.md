# API Load Testing with JMeter

这是一个使用JMeter进行API压测的示例项目，配置为10 QPS（每秒查询率）。

## 项目结构

- `api_server.py`: 模拟的API服务
- `api_load_test.jmx`: JMeter压测脚本
- `requirements.txt`: 项目依赖

## 如何运行压测

### 1. 启动API服务

```bash
# 安装依赖
pip install -r requirements.txt

# 启动API服务器
python api_server.py
```

API服务器将在 `http://localhost:5000` 上运行。

### 2. 运行JMeter压测

确保您已经安装了JMeter，然后运行以下命令：

```bash
# 使用JMeter GUI模式
jmeter -n -t api_load_test.jmx -l results.jtl -e -o report/

# 或者直接启动GUI界面
jmeter -t api_load_test.jmx
```

## 压测配置说明

- **并发线程数**: 10个线程
- **目标吞吐量**: 10 QPS
- **预热时间**: 10秒
- **测试持续时间**: 300秒（5分钟）
- **测试接口**:
  - GET /api/test
  - GET /api/users
  - GET /health

## 测试断言

- 验证响应中包含 "status":"success" 字符串
- 验证HTTP状态码为200

## 压测结果

- 结果将保存在 `results.jtl` 文件中
- HTML报告将生成在 `report/` 目录下