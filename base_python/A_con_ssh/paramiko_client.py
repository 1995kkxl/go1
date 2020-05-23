import paramiko
import configparser

class ParamikoClinet:
    def __init__(self,config_str,section):
        self.config = configparser.ConfigParser()
        self.config.read('config.ini')
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        self.sftp_client = None
        self.client_state = 0 #未连接
        self.section = section

    def connect(self):
        try:
            self.client.connect(
                hostname=self.config.get(self.section,'host'),
                port=self.config.getint(self.section,'port'),
                username=self.config.get(self.section,'username')
                ,password=self.config.get(self.section,'password'),
                timeout=self.config.getfloat(self.section,'timeout'))
            self.client_state = 1 #连接成功
        except Exception as e:
            print(e)
            try:
                self.client.close()
            except:
                pass

    def run_cmd(self,cmd_str):
        stdin,stdout,stderr=self.client.exec_command(cmd_str,get_pty=True)
        for line in stdout:
            print(line)


    def get_stp_client(self):
        if self.client_state == 0:
            self.connect()#如果未连接，使用连接
        if not self.sftp_client:
            self.sftp_client  = paramiko.SFTPClient.from_transport(self.client.get_transport())
        return self.sftp_client

