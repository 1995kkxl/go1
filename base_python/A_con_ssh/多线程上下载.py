from paramiko_client import ParamikoClinet
import threading
import time

#加线程锁
lock = threading.Lock()
num = 0

def upload_func():
    global num #全局的锁
    lock.acquire()
    num = num+1
    lock.release()
    client = ParamikoClinet('config.ini')
    client.connect()
    sftp_client = client.get_stp_client()
    sftp_client.put('up.txt','/root/allen/code/up.txt')
    print('upload finished')

def download_func():
    global num  # 全局的锁
    lock.acquire()
    num = num + 1
    lock.release()
    client = ParamikoClinet('config.ini')
    client.connect()
    sftp_client = client.get_stp_client()
    sftp_client.get('/root/allen/code/data.txt','data.txt')
    print("download finished")

def operate_one_machine():
    upload_thread = threading.Thread(target=upload_func)
    download_thraed = threading.Thread(target=download_func)
    upload_thread.start()
    download_thraed.start()
    upload_thread.join()
    download_thraed.join()

if __name__ == '__main__':
    operate_one_machine()