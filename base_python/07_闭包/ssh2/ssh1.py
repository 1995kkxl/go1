import paramiko
import configparser
from multiprocessing import Pool
import time


class ParamikoClient:
    def __init__(self, file, section):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.config = configparser.ConfigParser()
        self.config.read(file)
        self.section = section

    def connect(self):
        try:
            self.client.connect(
                hostname=self.config.get(self.section, 'host'),
                port=self.config.getint(self.section, 'port'),
                username=self.config.get(self.section, 'username'),
                password=self.config.get(self.section, 'password'),
                timeout=self.config.getfloat(self.section, 'timeout')
            )
        except Exception as e:
            print(e)
            try:
                self.client.close()
            except:
                pass



    def runcmd(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        return stdout.read().decode()




#执行

def process(section):
    client = ParamikoClient('config.conf', section)
    print(section)
    client.connect()
    a = client.runcmd('bash /root/ping.sh')
    print(a, end='')


process('ssh1')

# task_num = 1 #几台机器
#
# if __name__ == '__main__':
#     # single process time;
#     # start = time.time()
#     pool = Pool()
#     process('ssh1')
#     # # process('ssh2')
#     # # process('ssh3')
#     # print(time.time() - start)
#
#     # multi process time;
#     start = time.time()
#     task_num = task_num + 1
#     for i in range(1, task_num):
#         section = 'ssh' + str(i)
#         pool.apply_async(process, args=(section,))
#     pool.close()
#     pool.join()
#     print(time.time() - start)