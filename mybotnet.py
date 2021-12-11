import paramiko
import sys

def sshclient(host,user,passw, cmd):
    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        s.connect(hostname=host, username=user, password=passw)
    except Exception as e:
        print(e)
        print("连接出现错误！")
        sys.exit()

    xxx,sxxxt,sxxxxr=s.xxxc_xxxxxx(cmd)
    result=stdout.read()
    print(str(result,encoding='utf-8'))
    s.close()

if __name__=='__main__':
    mysql={
        xxxxxxxxxx
        xxxxxxxxxxxx
        xxxxxxxxxx
        xxxxxxxxxxx
    }
    for ip_key,v in mysql.items():
        xxxxxxx(host=ip_key, user=v.get("user"), passw=v.get("passw"), cmd=v.get("cmd"))
    print("ok")
