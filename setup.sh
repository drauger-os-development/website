#!/bin/bash
# -*- coding: utf-8 -*-
#
#  setup.sh
#
#  Copyright 2021 Thomas Castleman <contact@draugeros.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
set -Ee
set -o pipefail
port="$1"
if [ "$port" == "" ]; then
	port="80"
fi
echo "Installing Dependencies . . ."
sudo apt install --assume-yes $(<requirements_apt.txt)
username=$(whoami)
echo "Configuring your system . . ."
sudo cp -v website.nginx_conf /etc/nginx/sites-available/website.conf
sudo cp -v website.service /etc/systemd/system/website.service
sudo sed -i "s:<path to>:$PWD:g" /etc/nginx/sites-available/website.conf
sudo sed -i "s:<port>:$port:g" /etc/nginx/sites-available/website.conf
sudo sed -i "s:<path to>:$PWD:g" /etc/systemd/system/website.service
sudo sed -i "s:<username>:$username:g" /etc/systemd/system/website.service

# Only bother trying to delete this file if it exists
if [ -f /etc/nginx/sites-enabled/default ]; then
	echo "Disabling default site . . ."
	sudo rm -fv /etc/nginx/sites-enabled/default
fi

echo "Enabling site and restarting Nginx . . ."
sudo systemctl enable website
sudo ln -sv /etc/nginx/sites-available/personal_website.conf /etc/nginx/sites-enabled/website.conf
sudo systemctl restart nginx
sudo systemctl start website
git log | grep "^commit " | head -n1 | awk '{print $2}' > .git_commit_number
echo "Please ensure port $port is open so that the website may be exposed to the network"
