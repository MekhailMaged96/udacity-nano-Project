Documentation
-------------
Restaurant Menu Application it perform CRUD operation you can add,edit,read,delete Restaurant and menu and provide 
(google sign in outh) users can log with thier google accounts and you don not have to save passwords or worry about it google it provide to u  and every user have his own restaurant and menu and can not modify another user restaurnts or menus  



Software
--------
1- python version 2
2- vagrant and virtual box 
3- OAuth 2.0 to enable google log in 
4- Flask FrameWork

for development you  should know 
1- html5 / css
2- javascript and jquery for OAuth 2.0
3- bootstrap 3
4- Python 
5- json 
6- flask

 OAuth2.0
---------
You will need to sign up for a google account and set up a client id and secret.
Visit: http://console.developers.google.com for google setup


run
----
1- copy the project to the vagrant directory 

2- load vagrant and log in 

3- go to project location 

4- run  database_setup.py  follow this command:
	$ python database_setup.py
 
5- then lotsofmenus.py follow this command:
	$ python lotsofmenus.py

6- finally run  main.py follow this command:
	$ python manin.py

8- go to this link after run main.py localhost:5000

9 - go to  login page by click button login or follow this link localhost:5000/login\

10- to see restaurant menu click show menu 

JSON
-----

after follow the steps to run 

you can access json 

1-for all  restaurants:localhost:5000/restaurant/JSON 

2-for specfic restaurant menus : localhost:5000/restaurant/<int:restaurant_id>/menu/JSON

3-for specfic menu:localhost:5000/restaurant/<int:restaurant_id>/menu/<int:menu_id>/JSON



Hints
-----
Template file contains Html files 

and Static file contains CSS/JS/photos files

you can also add another oauth providers like facebook / wiki 

License
--------
Copyright by Mekhail Maged 





