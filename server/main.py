#!/bin/python3

from world import World
from server import MyTcpHandler
from common import *

import db
import socketserver


if __name__ == '__main__':
    printt("Welcome to TTR server...")


    db._init()
    g_db = db.DB()
    db.setDb(g_db)

    if not g_db.connect():
        printt("Can not connect to DB")
        quit(-1)

    printt("Succeed to connect to DB")

    world = World()

    port = 2018
    
    server = socketserver.TCPServer(("localhost", port), MyTcpHandler)

    if server == None:
        printt("Can not listen socket port: " + str(port))
    else:
        printt("Start to listen socket port: " + str(port))

    server.db = db
        
    server.serve_forever()

    #while True:
    #    world.processMsg()
    #    world.update()
        

