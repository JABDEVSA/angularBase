#!/bin/sh

msg=$1

if [ "${msg}" = "" ];
then
    echo "Please enter a commit message"
else
    clear
    git add .
    git commit -m ${msg}
    git push
fi


