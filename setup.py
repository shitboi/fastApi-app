import os
import subprocess


# # clone repo and move to dir (useful for authomated deployment)
# subprocess.run('git clone https://github.com/shitboi/fastApi-app.git')

print(os.getcwd())
try:
    os.chdir('fastApi-app')
except Exception as e:
    print(f'change directory Error - {e}')

#install apt package
subprocess.run('apt install python3-fastapi python3-pandas python3-uvicorn nginx -y', shell=True)

#get server ipAddress
com = subprocess.run('ip a |grep "global eth0" |head -n 1',
                     shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
if com.returncode==0:
    ip = com.stdout.decode().split(' ')[5].split('/')[0]

    # replace servername with serverIP address
    replace_com = f"sed -i 's/serverPublicIP/{ip}/g' fastapi_nginx"
    replacement = subprocess.run(replace_com, shell=True)
    if replacement.returncode==0:
        # copy file to nginx site-enabled dir and restart nginx
        subprocess.run('cp fastapi_nginx /etc/nginx/sites-enabled/fastapi_nginx && service nginx restart', shell=True)

        # start fastapi app
        subprocess.run('python3 -m uvicorn main:app')


