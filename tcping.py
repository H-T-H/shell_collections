import socket

def tcping(ip, port, timeout=0.5):
    try:
        socket.setdefaulttimeout(timeout)  # 设置超时时间（秒）
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"{ip}: Port {port} is open")
        else:
            print(f"{ip}: Port {port} is closed")
        sock.close()
    except socket.error as e:
        print(f"{ip}: Error occurred: {e}")

def main():
    file_path = "ip2.txt"
    with open(file_path, "r") as file:
        for line in file:
            ip = line.strip()
            tcping(ip, 22)

if __name__ == "__main__":
    main()
