from paramiko_client import ParamikoClinet
import gevent
import time
import os
import configparser
from multiprocessing import Pool

# client = ParamikoClinet('config.ini','ssh')
# client.connect()
# client.run_cmd('bash /root/t1.sh')

task_num = 2
def process(section):
    client = ParamikoClinet('config.ini', section)
    client.connect()
    client.run_cmd('date')

def gevent_process(section):
    client = ParamikoClinet('config.ini', section)
    gevent.sleep(0)
    client.connect()
    gevent.sleep(0)
    client.run_cmd('date')


if __name__ == '__main__':
    # process('ssh0')
    events = []
    for i in  range(task_num):
        section = 'ssh'+str(i)
        event = gevent.spawn(process,section)
        events.append(event)
    gevent.joinall(events)



# if __name__ == '__main__':
#     pool = Pool()
#     for i in range(task_num):
#         section = 'ssh' + str(i)
#         #process(section)
#         pool.apply_async(process, args=(section,))
#         print(section)
#     pool.close()
#     pool.join()


#执行命令开始
# begin = time.time()
# query_num = 100
# query_frequency = 0.2
#
# while query_num>0:
#     now = time.time()
#     if now - begin > query_frequency:
#         client.run_cmd('date')
#         begin = now
#         query_num =query_num-1
#执行命令结束

#文件上传

# sftp_client = client.get_stp_client()
# def put_callback(size1,size2):
#     print(size1,size2)
# sftp_client.put('config.ini','/root/config.ini',put_callback)
# client.run_cmd('ls')



#更新

# sftp_client = client.get_stp_client()
# def get_callback(size1,size2):
#     print(size1,size2)
# client.run_cmd('ls')
#
# #to do
# ori_total_seq = 0
# class BaseFileIngo:
#     def __init__(self,name,seq):
#         self.name = name
#         self.seq =seq
#
# def load_base_file_info():
#     pass
#
# files_map = {}
# #sftp_client.get('/root/allen/res.txt','res.txt',get_callback)
# client.run_cmd('ls')
# config = configparser.ConfigParser()
# config.read('res.txt')
# total_seq = config.get('total','req')
# if total_seq != ori_total_seq:
#     sectons = config.sections()
#     for secton in sectons:
#         if secton == 'files':
#             for conf in config.items(secton):
#                 name = conf[0]
#                 seq = conf[1]
#                 print(name,seq)
#                 if name in files_map:
#                     file = files_map[name]
#                     if file.seq != seq:
#                         #download it
#                         sftp_client.get('/root/allen/data'+name,'code/'+name)
#                 else:
#                     sftp_client.get('/root/allen/data'+name,''+name)
#                     info = BaseFileIngo(name,seq)
#                     files_map[name] = info




#从服务器下载最新资源更新
# class BaseFileInfo:
#     def __init__(self, name=None, seq=None):
#         """
#         :param name: 文件名
#         :param seq: 文件版本号
#         conf.get('total', 'req') 为大版本的版本号
#         """
#         self.name = name
#         self.seq = seq
#         self.client = ParamikoClinet('config.ini')
#         self.sftp_client = self.client.get_stp_client()
#
#         self.conf = configparser.ConfigParser()
#         self.conf.read('res.txt')
#         self.total_seq = self.conf.get('total', 'req')
#
#         self.ori_total_seq = 0
#         self.file_map = {}  # 存放 [] 下的每一项文件的名称及版本号
#
#
#
#     @staticmethod
#     def get_callback(size1, size2):
#         """
#         :param size2: 服务器端文件大小
#         :param size3: 本地文件大小
#         :return:
#         """
#         print(size1, size2)
#
#     def run(self):
#         print("running")
#         """
#         下载服务器端文件版本的序列号记录文件 res_des.txt
#         conf.sections() 这个东西为 res_des.txt文件中的[file] 每一项[]内的内容
#         :return:
#         """
#         self.client.sftp_client.get('/root/allen/res.txt', r'D:\go1\base_python\A_con_ssh\res.txt', self.get_callback)
#
#         if self.total_seq != self.ori_total_seq:    # 比较本地与服务器端版本号是否一致
#             sectons = self.conf.sections()
#             print(sectons)
#             # res.txt 中的 []
#             for secton in sectons:
#                 if secton == 'files':
#                     for conf in self.conf.items(secton):  # ('t1.txt', '1') 为 []下的每一个文件名称对应的版本号
#                         name = conf[0]
#                         seq = conf[1]
#                         print(conf[0],conf[1])
#                         if name in self.file_map:  # 文件名称在，版本号不同进行文件更新
#                             file = self.file_map[name]
#                             if file.seq != seq:
#                                 self.sftp_client.get('/root/allen/' + name, r'D:\go1\base_python\A_con_ssh' + os.sep + name)
#                         else:
#                             self.sftp_client.get('/root/allen/' + name, r'D:\go1\base_python\A_con_ssh' + os.sep + name)
#                             info = BaseFileInfo(name, seq)  # 文件名称及版本号
#                             self.file_map[name] = info
#
# if __name__ == '__main__':
#     BaseFileInfo().run()
