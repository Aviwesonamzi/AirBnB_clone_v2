#!/usr/bin/env bash
# Script to set up web servers for deployment of web_static

# Update and install Nginx if not already installed
if ! dpkg -l | grep -q nginx; then
    apt-get update -y
    apt-get install nginx -y
fi

# Create required directories if they do not already exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# Create a fake HTML file to test Nginx configuration
echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

# Create a symbolic link, recreate it if it already exists
if [ -L /data/web_static/current ]; then
    rm /data/web_static/current
fi
ln -s /data/web_static/releases/test/ /data/web_static/current

# Give ownership of the /data/ folder to the root user and group
chown -R root:root /data/

# Remove duplicate location /404.html block in Nginx configuration
sed -i '/location \/404.html/d' /etc/nginx/sites-available/default

# Update Nginx configuration to serve content
NGINX_CONFIG="/etc/nginx/sites-available/default"
if ! grep -q "location /hbnb_static" $NGINX_CONFIG; then
    sed -i '/server_name _;/a \ \n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $NGINX_CONFIG
fi

# Restart Nginx to apply changes
service nginx restart

exit 0
