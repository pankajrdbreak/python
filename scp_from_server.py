import os
import subprocess
#p=subprocess.Popen(["scp","file.txt","ubuntu@35.154.222.116:/home/ubuntu"])
#sts= os.waitpid(p.pid, 0)
#subprocess.run('scp -i new.pem ubuntu@35.154.222.116:/home/ubuntu/file.txt .')
#cmd='scp -i new.pem ubuntu@35.154.222.116:/home/ubuntu/file.txt .'
#subprocess.run(cmd)
list_dir = subprocess.Popen(["scp", "-i", "new.pem", "ubuntu@35.154.222.116:/home/ubuntu/abc.txt", "."])
list_dir = subprocess.Popen(["scp", "-i", "new.pem", "ubuntu@35.154.222.116:/home/ubuntu/abc2.txt", "."])
list_dir = subprocess.Popen(["scp", "-i", "new.pem", "ubuntu@35.154.222.116:/home/ubuntu/abc3.txt", "."])
list_dir = subprocess.Popen(["scp", "-i", "new.pem", "ubuntu@35.154.222.116:/home/ubuntu/abc4.txt", "."])
list_dir.wait()