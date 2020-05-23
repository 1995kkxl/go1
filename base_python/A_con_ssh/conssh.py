import paramiko
import configparser

config = configparser.ConfigParser()
config.read('config.ini')
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
try:
    client.connect(hostname=config.get('ssh','host'),port=config.getint('ssh','port'),username=config.get('ssh','username')
                   ,password=config.get('ssh','password'),timeout=config.getfloat('ssh','timeout'))
except Exception as e:
    print(e)
    try:
        client.close()
    except:
        pass
stdin,stdout,stderr = client.exec_command('cat /root/ping.sh')
for line in stdout:
    print(line)