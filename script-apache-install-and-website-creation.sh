#!/bin/bash

echo "installing apache server"
sudo yum -y install httpd

echo "enabling apache server"
sudo systemctl enable httpd.service

echo "starting apache server"
sudo systemctl start httpd.service

echo "If you open the security settings for port 80 on your server, you should see the apache start page"

#landingpage.html is a static HTML page that the user created and 
#saved the  home directory of the user
echo "add static HTML page to apache server"
sudo sh -c 'cat landingpage.html > /var/www/html/landingpage.html'

#restart apache server
echo "restarting apache server"
sudo service httpd restart
