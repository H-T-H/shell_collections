#!/bin/bash

# 更新系统
apt update

# 安装 Shadowsocks
apt install -y shadowsocks-libev

# 创建配置文件
tee /etc/shadowsocks-libev/config.json > /dev/null <<EOF
{
    "server":"0.0.0.0",
    "server_port":1,
    "password":"teddysun.com",
    "timeout":300,
    "method":"aes-256-gcm"
}
EOF
# 启动 Shadowsocks 服务 
systemctl restart shadowsocks-libev

# 设置开机自启动
systemctl enable shadowsocks-libev
