from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return '🍉 Xuanzi 舆情服务运行中！访问 /run-task 启动任务'

@app.route('/run-task')
def run_task():
    try:
        subprocess.run(["python3", "crawler.py"])
        return '✅ 舆情任务已执行完毕'
    except Exception as e:
        return f'❌ 出错: {str(e)}'
