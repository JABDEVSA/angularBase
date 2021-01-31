# Angular and our REST base application

This repo is ment for the very start of a project, here we have an example of a http-service that is created in python also known as a REST backend, please refer to the http-service folder/dir.Then we have the webapp, this is based on our very cool Angular systems and packages. 

So let's get started, it is recommended to clone the repo first:
```
    $ git clone git@github.com:JABDEVSA/angularBase.git
    $ or
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

Okay so for that we have a couple of requieremnets here:
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

Now we develop our webapp and push to git, we only push what is needed and then we clone the project to a new PC system now we need to get all the models inplace to have the system working again, for this we have the following procedure, please follow these steps to install webapp on a new PC:

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

## Have fun and enjoy

If there is any issues please contact me for guidance.


