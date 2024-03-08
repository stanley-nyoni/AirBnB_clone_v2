#!/usr/bin/env bash
# Install nginx and create folders

#Install nginx
sudo apt-get -y update
sudo apt-get -y install nginx
sudo ufw allow 'Nginx HTTP'

#Create necessary folders
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo touch /data/web_static/releases/test/index.html

#Add content to index.html
echo "<html>
    <head>
    </head>
    <body>
        Holberton School
    </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

#Create a symbolic link
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

#Change ownership of /data/
sudo chown -R ubuntu:ubuntu /data/

#Update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sudo sed -i "/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; }" /etc/nginx/sites-enabled/default

#Restart nginx
sudo service nginx restart
