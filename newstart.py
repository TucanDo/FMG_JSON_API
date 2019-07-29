import paramiko

ssh = paramiko.SSHClient()
ssh.connect(172.31.200.77, username=admin, password="")
ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("get system status")