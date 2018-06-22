Documentation
-------------
 a large database with over a million rows is explored by building complex SQL queries, in this project 
 
it will analysis the a large database and  draw business conclusions from data.

Software Requriments
-------------------
1-Python3
2-Vagrant
3-VirtualBox

Install
--------
1- install Vagrant and Virtual Box

2- the file (Logs Analysis Project)  contain newsdata.sql and log_data.py

3- Launch the Vagrant VM inside Vagrant sub-directory  in the file Logs Analysis Project using command:
   $ vagrant up
   
4- Log into the VM using command :
   $ vagrant ssh
  
5- after log in change directory to / vagrant using command:
   $ cd /vagrant 
   
6- From the vagrant directory inside the virtual machine,run log_data.py using command :
   $ python3 log_data.py

Hints
-----  
1- if you wanna to see data in database after log into vm use command :
   psql -d news -f newsdata.sql
   
2- The DataBase contain Three Tables :
		The authors table      : includes information about the authors of articles.
		The articles table     : includes the articles themselves.
		The log table includes : one entry for each time a user has accessed the site.

     
   
   
   
License
--------
Copyright by Mekhail Maged 
   
   
   
   