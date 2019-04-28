#!/bin/sh
sudo -u postgres dropdb csGo
sudo -u postgres psql -c 'drop user cr'
sudo pip3 uninstall psycopg2 protobuf
sudo apt remove postgresql libpq-dev python3-pip
