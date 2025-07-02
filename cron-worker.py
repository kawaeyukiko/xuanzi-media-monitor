import requests

try:
    res = requests.get("https://xuanzi-media-monitor.onrender.com/run-task")
    print("✅ 请求完成，返回内容：", res.text)
except Exception as e:
    print("❌ 请求失败：", str(e))
