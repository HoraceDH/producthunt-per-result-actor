#!/bin/sh

# 启动虚拟显示器
Xvfb :99 -screen 0 1920x1080x24 &

# 进程
python3 -m src
