# Angular and our REST base application

This repo is ment for the very start of a project, here we have an example of a http-service that is created in python also known as a REST backend, please refer to the http-service folder/dir.Then we have the webapp, this is based on our very cool Angular systems and packages. 

So lets get started, it is recommended to clone the repo first:
```bash
    $ git clone git@github.com:JABDEVSA/angularBase.git
    $ or
    $ git clone https://github.com/JABDEVSA/angularBase.git
```

note: if you are using the ssh option which is the best ensure that you have your ssh key installed on this github in security access that through settings.

Okay so now we have the Angular Base Repo on your PC cool, let's look at the following.

## To start this off

Create a new project in git with your project name, clone the repo to your PC and ensure that you clone this base repo aswel so we have the following standard, you will see once both repo's are cloned we copy the base project into the new project repo with the following:
```bash
` Create a new git dir named project
`   $ mkdir project
`
` Navigate to project
`   $ cd project
`
` Clone the base repo
`   $ git clone https://github.com/JABDEVSA/angularBase.git
`
` Clone the new repo
`   $ git clone <new_repo_link>
`
` Copy base into new project
`   $ cp -rf /angularBase/* /new_project
`
```

With this done confirm that you have all the files and then let's proceed with the following.

## The http-service things

This system makes use of python venv to build an enviroment where we have all our requiered packages, this is installed in one env dir, this makes it easy to work with the system and we do not make use of the systems packages. So let's do the following here:

Install venv:
```bash
` First install pip
`   $ sudo apt install python3-pip
`
` Then install venv
`   $ python3 -m pip install virtualenv
`
` Navigate to the http-service dir
`   $ cd http-service
`
` Then install the env dir
`   $ python3 -m venv env
`
` Activate the env with
`   $ source env/bin/activate
`
```

With this done we have a clean venv system with its own Python3 binary and packages, here we can do the following:
```bash
` Find the shebang of python3 for the applications
`   $ which python3
`
` Install packages
`   $ python3 -m pip install <package_name>
`
```

So we have an enviroment where we can setup a brand new project


#create a requirements.txt

pip freeze > requirements.txt

python3 -m venv env
source env/bin/activate
cd ..
pip3 install -r requirements.txt
