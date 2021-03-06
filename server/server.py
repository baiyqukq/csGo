import socketserver
import struct
import db

from datetime import datetime
from common import *
from pb.cmd_pb2 import *
from pb.account_pb2 import *

class MyTcpHandler(socketserver.BaseRequestHandler):
    def processMsg(self, cmd, data):
        t = datetime.now()

        if cmd == CS_CMD_LOGIN:
            msg = CsLogin()
            msg.ParseFromString(data)

            g_db = db.getDb()
            ret = g_db.login(msg.name, msg.password)

            msg = ScLogin()
            msg.res = ret

            self.sendMsg(SC_CMD_LOGIN, msg)
        else:
            printt("There is no processed message")

        cost = datetime.now() - t;
        printt("Process message[%d] cost: %s" % (cmd, str(cost)))

    def sendMsg(self, cmd, msg):
        data = msg.SerializeToString()
        head = struct.pack("!hhh", 6, len(data), cmd)
        self.request.send(head)
        self.request.send(data)

    def handle(self):
        head = self.request.recv(6)
        headLen, dataLen, cmd = struct.unpack("!hhh", head)
        
        if headLen != 6:
            printt("Data transfer format is error, head length is not 6")
            return

        data = self.request.recv(dataLen)

        #print("[%s]cmd: %d, dataLen: %d, data: %s" % (self.client_address[0], cmd, dataLen, repr(data)))

        self.processMsg(cmd, data)


