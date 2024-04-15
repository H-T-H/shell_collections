import base64

def generate_ss_link(ip, index):
    encryption_method = "aes-256-gcm"
    password = "teddysun.com"
    port = "1"
    
    # 拼接Shadowsocks链接格式
    ss_link = f"{encryption_method}:{password}@{ip}:{port}"
    
    # 进行Base64编码
    encoded_link = base64.b64encode(ss_link.encode()).decode()
    
    # 生成完整的Shadowsocks链接
    return f"ss://{encoded_link}#{index}\n"

# 读取ip.txt文件
with open("ip.txt", "r") as file:
    ips = file.readlines()

# 写入到output.txt并添加顺序编号
with open("output.txt", "w") as output_file:
    for index, ip in enumerate(ips, start=1):
        ip = ip.strip()  # 去除换行符
        ss_link = generate_ss_link(ip, index)
        output_file.write(ss_link)
