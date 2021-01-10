confwww="/var/www/html/.htaccess"
confDir="ConfigFiles"
libFile="/home/jab/.local/share/virtualenvs/hydroclear-vT5rmpVR"
libDir="Libs"
wwwHydro="/var/www/html/hydroclear/*"
wwwDir="webapp"
pythonFile="Libs/hydroclear-vT5rmpVR/lib/python3.8/site-packages/hydroclear/*.*"
pythonDir="hydroclear"

cp ${confwww} ${confDir}
cp -rf ${libFile} ${libDir}
sudo cp -rf ${wwwHydro} ${wwwDir}
sudo chown -R jab:jab ${wwwDir}
cp  ${pythonFile} ${pythonDir}

