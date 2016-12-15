#!/bin/bash 
#THIS IS FILE 1 OF A 2-FILE CRON JOB 
#FILE 1 IS A SCRIPT THAT CHECKS THE SERVER EVERY HOUR AND EMAILS YOU IF NO ONE LOGGED IN: check-apache-server.sh
#FILE 2 CREATES A CRONTAB TO ACCESS THE SCRIPT IN FILE 1 : cron-assignment.crontab

#FYI:
#The cron daemon is a long-running process that executes commands at specific dates and times. 
#You can use this to schedule activities, either as one-time events or as recurring tasks.
#For commands that need to be executed repeatedly (e.g., hourly, daily, or weekly), you can use the crontab command. 
#The crontab command creates a crontab file containing commands and instructions for the cron daemon to execute.

#DESCRIPTION OF ASSIGNMENT:
#Your script should be croned to run once an hour and email you if there is no activity on your server and no one logged in.

#HERE IS THE SCRIPT FOR THIS FILE OF THE ASSIGNMENT:
# The  -l  option causes the current crontab to be displayed on standard output.
#crontab -l
#number of users logged in is $users
users=$( /usr/bin/who | grep -c "" )
#count the number of apache users (1 if apache is up, 2 if not), store as $apachestatus
apachestatus=$( ps auxw | grep apache | grep -c "")
if [ "$apachestatus" -eq "0" && "$users" -lt "1" ]
then
        echo “ Yikes, server down! The aws apache server with ip address @54.86.131.96 is DOWN. Also, there no one is logged on to the server. Put on your cape and fix it! ”
       #Echo “This is a message” | mail -s “This is a subject” youremail@example.com
fi
#chmod +x
