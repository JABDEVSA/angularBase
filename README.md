# Angular and our REST base application

This repo is ment for the very start of a project, here we have an example of a http-service that is created in python also known as a REST backend, please refer to the http-service folder/dir.Then we have the webapp, this is based on our very cool Angular systems and packages. 

So let's get started, it is recommended to clone the repo first:
```
    $ git clone git@github.com:JABDEVSA/angularBase.git
      or
    $ git clone https://github.com/JABDEVSA/angularBase.git
```

note: if you are using the ssh option which is the best ensure that you have your ssh key installed on this github in security access that through settings.

Okay so now we have the Angular Base Repo on your PC cool, let's look at the following.

## To start this off

Create a new project in git with your project name, clone the repo to your PC and ensure that you clone this base repo aswel so we have the following standard, you will see once both repos are cloned we copy the base project into the new project repo with the following:
```
  Create a new git dir named project
    $ mkdir project
 
  Navigate to project
    $ cd project
 
  Clone the base repo
    $ git clone https://github.com/JABDEVSA/angularBase.git
 
  Clone the new repo
    $ git clone <new_repo_link>
 
  Copy base into new project
    $ cp -rf /angularBase/* /new_project
 
```

With this done confirm that you have all the files and then let's proceed with the following.

## The http-service

This system makes use of python venv to build an enviroment where we have all our required packages, this is installed in one env dir, this makes it easy to work with the system and we do not make use of the systems packages. So let's do the following here:

Install venv:
```
  First install pip
    $ sudo apt install python3-pip
 
  Then install venv
    $ python3 -m pip install virtualenv
 
  Navigate to the http-service dir
    $ cd http-service
 
  Then install the env dir
    $ python3 -m venv env
 
  Activate the env with
    $ source env/bin/activate
 
```

With this done we have a clean venv system with its own Python3 binary and packages, here we can do the following:
```
  Find the shebang of python3 for the applications
    $ which python3
 
  Install packages
    $ python3 -m pip install <package_name>
 
```

So we have an enviroment where we can setup a brand new project of the REST service, so we can develop our apps and then install packages now we are done and we want to push to the project repo, and for this we do not want to include the env file. To ensure that we do not include all the env files we have a gitnore file. This file tells git not to copy a specific dir, have a look you will see the exclusion.

So let's say we have a new PC system and we copy the repo to it, how do we install the required packages?

pip to the rescue, we can make a copy of all required packages and install them by using this file ie requirements.txt, so first lets generate on by execurting the following command, please ensure that you venv env is activated when doing this so here we go, first project is done and you want to backup all packages:

```
 Ensure that you are in the root dir of the project

 Backup/Create a list of required packages with
    $ pip freeze > requirements.txt
```

This will create a requirements.txt file for you, so now we have a requirements.txt file in project root, from here we will install the repo on a new PC, then create the venv env dir in http-services, the start the venv as shown above then we will use the following command to install all required packages

```
 Install packages to venv, this is done from root dir where requirements.txt lives
    $ python3 -m pip install -r requirements.txt
```

This will install all your packages cool ne!

## The webapp

I will recomend to delete the webapp dir and create a new one and the greate a new project in it, the project that I am talking about is angular. Obviously this will be done only on the creation of a new clean project structure not an completed one please use commen sense when working here.

Okay so for that we have a couple of requirements here:
```
 First install nodejs
    $ sudo apt install nodejs
    $ node -v
    $ sudo apt install npm
    $ npm -v
```

Good now we have nodejs and npm installed, let's install angular/cli:

```
 Install Angular cli
    $ npm install -g @angular/cli

Create the webapp dir/app
    $ sudo ng new webapp
```

Now just like the http-service we have a new clean struture and all, we can start developing, please ensure that you setup your credentials with github on your PC before creating the new web-app you can do this by:

```
    $ git config --global user.name "YourName"
    $ git config --global user.email "YourEmail"
```

This will setup your enviroment with your git project and ensure that we do not copy overloaded dir's like node_modules and all the other parts that will overload the project size. Once again if you look in the root dir of webapp you will see we have a gitnore file which tells git to exclude these files, it works no need to change it just add if you need to.

Now we develop our webapp and push to git, we only push what is needed and then we clone the project to a new PC system now we need to get all the models in place to have the system working again, for this we have the following procedure, please follow these steps to install webapp on a new PC:

```
 Clone the repo
    $ git clone <repo_link>

 Navigate to webapp
    $ cd projectName/webapp

 Install webapp with
    $ npm install

 After install serve with
    $ ng serve --host 0.0.0.0
```

And there you go we have http-service installed and webapp.

I will need to have a automated script that will do this for us, the next in this project will be unit testing and then also docker images this will follow soon.

## MySql works

For this and any type of project we need a database, this can be a remote or a local style database, for these projects we are initially using a local database and it is a real pain to do this locally if this is your first time, so let's setup a dummy database here.

note: this example is for developemnt purposes and please ensure that on production the credentials are changed and secure, this will expose your database if left like this.

Lets install and configure our mysql database:

```
 Install mysql on ubuntu
    $ sudo apt install mysql-server

 Please note that you installed it using sudo so change to root and login
    $ sudo su
    $ mysql
    
 You are now logged in as root, create a new user with the following
    $ mysql> CREATE USER 'jab'@'localhost' IDENTIFIED BY '222';
    $ mysql> GRANT ALL PRIVILEGES ON * . * TO 'jab'@'localhost';
    $ mysql> UPDATE mysql.user SET plugin = 'caching_sha2_password' where user = 'jab';
    $ mysql> FLUSH PRIVILEGES;

 Now logout with ctrl-d and again ctrl-d you are back in your user
 Login to mysql as your user in this case jab with
    $ mysql -u jab -p
    $ enter password

 If you get access you are done!
 If not check creds as root and ensure all info is correct
    $ mysql> select user, host, plugin from mysql.user;

    +------------------+-----------+-----------------------+
    | user             | host      | plugin                |
    +------------------+-----------+-----------------------+
    | debian-sys-maint | localhost | caching_sha2_password |
    | jab              | localhost | caching_sha2_password |
    | mysql.infoschema | localhost | caching_sha2_password |
    | mysql.session    | localhost | caching_sha2_password |
    | mysql.sys        | localhost | caching_sha2_password |
    | root             | localhost | auth_socket           |
    +------------------+-----------+-----------------------+
    6 rows in set (0.00 sec)

```

With the DB setup you can proceed to the configurations file to connect.

## Config file

This configurations file makes use of yaml to register all credentials and port configurations needed to setup and run the project. It is quite self explandatory, if we need to have other, additional or new configurations just add it and like the main.py application with the detail.

```
    #Logging System Details
    logFileLocation : /home/jab/log/hydro/
    infoLogFile : hydInfo.log
    debuglogFile : hydDebug.log

    #Database system details
    dbuserName : jab
    dbpassword : 222
    dbhost : 127.0.0.1
    dbname : hydroclear

    #CherryPi Settings
    chpHost : 0.0.0.0
    chpPort : 50091

```

This file must be in place for the system to start-up and run.

## The http-service files

In the http-service we have a core files:
```
    --http-service
     |--main
     |     |-main.py
     |-httpservice.py
     |-logger.py
     |-mysqldrv.py

```

The main.py application is our initial entry point it will read the config file and setup the rest.

The httpservice.py file is our REST application making use of flask under cherrypy to serve it.

The logger.py file for logging, at this moment please look in ${pwd}/log/projectName/projectName_Info.log or Debug.log. Please note this is for development, experimental and excersize purposes this will be replaced with python logger soon.

The mysqldrv.py for the mysql operations needed.

To start this backend do the following:
```
    $ cd httpservice
    $ ./main/main.py

 For any development please source env/bin/activate

```


## Have fun and enjoy

If there is any issues please contact me for guidance.


