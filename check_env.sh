#!/bin/bash
# 测试环境检查脚本：在 Linux 服务器上快速确认测试所需环境是否就绪

echo "===== 系统信息 ====="
uname -a
echo ""

echo "===== Python 版本 ====="
python3 --version
echo ""

echo "===== 关键命令是否可用 ====="
for cmd in python3 pip3 git curl wget docker adb; do
    if command -v "$cmd" > /dev/null 2>&1; then
        echo "[OK]   $cmd -> $(command -v $cmd)"
    else
        echo "[MISS] $cmd 未安装"
    fi
done
echo ""

echo "===== 当前目录与磁盘空间 ====="
pwd
df -h . | tail -1
echo ""

echo "===== 最近 5 分钟的系统日志（/var/log/syslog 或 messages） ====="
LOG_FILE=""
[ -f /var/log/syslog ] && LOG_FILE=/var/log/syslog
[ -f /var/log/messages ] && LOG_FILE=/var/log/messages
if [ -n "$LOG_FILE" ]; then
    tail -n 5 "$LOG_FILE"
else
    echo "未找到系统日志文件"
fi
echo ""

echo "===== 环境检查完成 ====="
