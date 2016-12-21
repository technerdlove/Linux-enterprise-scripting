#!/usr/bin/python

import boto3
import base64
import pprint

ec2 = boto3.resource('ec2')
client = boto3.client('ec2')

amazon_image = 'ami-2051294a'                                       # This will launch a red hat instance
amazon_instance = 't2.micro'                                        # we've been working with micro's, if you use Amizon Linux, you could launch a nono
amazon_pem_key = 'load-ballancer-static-content'                    # the name of the key/pem file you would like to use to access this machine
firewall_profiles = ['launch-wizard-2']                             # the security group name(s) you would like to use, remember, this is your firewall, make sure the ports you want open are open

print(amazon_image)
print(amazon_instance)
print(amazon_pem_key)

def launch_test_instance():

   instances = ec2.create_instances(
      ImageId = amazon_image,
      InstanceType = amazon_instance,
      MinCount=1,
      MaxCount=1,
      KeyName = amazon_pem_key,
      SecurityGroupIds = firewall_profiles,
      UserData="""#!/usr/bin/python
# The purpose of this script is to configure and install a django server without needing to enter sudo
# This first line is very important.  You should import os first because of the numerous system calls in the script.
import os, sys
# This installs apache web server
def install_apache():
	print('installing apache server')
	os.system('sudo yum -y install httpd')
	print('enabling apache server')
	os.system('sudo systemctl enable httpd.service')
	print('starting apache server')
	os.system('sudo systemctl start httpd.service')
	print('If you open the security settings for port 80 on your server, you should see the apache start page')
install_apache()

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

# Here the script installs the django server with python and virtualenv
def install_django():
	print('installing django')
	os.system('python --version')
      	os.system('rpm -iUvh https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-release-7-8.noarch.rpm')
install_django()
def install_pip():
	os.system('yum -y install python-pip')
	print('installing python-pip')
install_pip()
def install_virtualenv():
	os.system('cd /opt')
	os.system('pip install virtualenv')
	os.system('cd /opt')
      	os.system('mkdir django')
      	os.system('sleep 5')
      	os.system('cd django')
	os.system('virtualenv django-env')
	print('installing virtual-env')
install_virtualenv()

# Here the script activates the django server
def activate_virtualenv():
	os.system('source /opt/django/django-env/bin/activate')
	os.system('which python')
	os.system('chown -R ec2-user /opt/django')
	os.system('pip install django')
	os.system('django-admin --version')
	os.system('django-admin startproject project1; exists_ok=true')
	os.system('tree project1')
	print('installing tree')
	print('installing django')
	os.system('python /opt/django/project1/manage.py runserver 0.0.0.0:8000&')
	print('done')
activate_virtualenv()
	"""
	)

#pprint.pprint(instances)


launch_test_instance()


            	


