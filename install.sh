#!/bin/bash
sudo apt install python3-pip postgresql libpq-dev
sudo pip3 install psycopg2 protobuf

sudo -u postgres createdb csGo
sudo -u postgres psql -f db/user.psql
psql csGo -f db/table.psql
psql csGo -f db/record.psql

protoc proto/*.proto --python_out=server/pb
protoc proto/*.proto --python_out=client/pb
