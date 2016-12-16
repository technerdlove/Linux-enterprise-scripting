#!/usr/bin/python
# The purpose of this script is to configure and install a django server without needing to enter sudo

# This first line is very important.  You should import os first because of the numerous system calls in the script.
import os
def install_apache():
       print('installing apache server')
       os.system('sudo yum -y install httpd')
       print('enabling apache server')
       os.system('sudo systemctl enable httpd.service')
       print('starting apache server')
       os.system('sudo systemctl start httpd.service')
       print('If you open the security settings for port 80 on your server, you should see the apache start page')
install_apache()

# Here the script installs the django server with python and virtualenv
def install_django():
	print('installing django')
install_django()
def install_pip():
	os.system('yum -y install python-pip')
	print('installing python-pip')
install_pip()
def install_virtualenv():
	os.system('cd /opt')
	os.system('pip install virtualenv')
	os.system('virtualenv django-env')
	print('installing virtual-env')
install_virtualenv()

# Here the script activates the django server
def activate_virtualenv():
	os.system('source /opt/django/django-env/bin/activate')
	os.system('which python')
	os.system('pip install django')
        os.system('django-admin --version')
        os.system('django-admin startproject project1; exists_ok=true')
	os.system('tree project1')
        print('installing tree')
	print('installing django')
	os.system('python /opt/django/project1/ manage.py runserver 0.0.0.0:8000&')
	print('done')
activate_virtualenv()

# This installs git and the tree package that belongs with git
def install_git():
	print('installing git')
	os.system('yum -y install git')
	os.system('git clone https://github.com/viridtyforever/NTI300-assignments')
install_git()
def install(package):
	print('installing package')
	os.system('yum -y install '+package)
install('tree')

# This installs the email service
def mailx():
	print('installing mailx')
	os.system('yum -y install mailx')
mailx()

# This installs security patches - specifically the dirty cow patch
def kernel():
	print('installing kernel')
	os.system('yum -y clean all && yum update kernel -y && yum -y reboot')
def verifying_dirty_cow():
	os.system('rpm -q --changelog kernel | grep CVE-2016-5195')
kernel()
verifying_dirty_cow()


            	


