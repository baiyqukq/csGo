Client/Server Go
================
A simple python client/server model, this is a very good start point.

Features
========
Language: Python 3</br>
DB: PostgreSQL</br>
Proto: Google Protobuf</br>
Network: TCP</br>

Initilize
=========
* Install Python3
* Install PostgreSQL
* Install psycopg2, like this:

```shell
pip install psycopg2
```

* Install protobuf
	* Download protobuf3.6.1 release package at github.com(uncompress, put protoc in $PATH)
	* Install python protobuf module

```shell
pip install protobuf
```

* Create database named "csGo", like this:

```shell
createdb csGo
```

* Create table, like this: 

```SQL
CREATE TABLE t_account(
	c_id		SERIAL		PRIMARY KEY,
	c_name		VARCHAR(15)	NOT NULL UNIQUE,
	c_password	vARCHAR(15)
);
```

* Insert a record, like this:

```SQL
INSERT INTO t_account(c_name, c_pasword) VALUES ('cr', 'q');
```

* Genrate python files with protobuf, like this:

```shell
protoc proto/* --python_out=server/pb
protoc proto/* --python_out=client/pb
```
or execute proto/mkproto.sh.

Start
=====
* Start server

```shell
python3 server/main.py
```

* Start client

```shell
python3 client/main.py
```
Author
======
baiyqukq@163.com
