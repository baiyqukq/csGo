import socket
import sys
import struct

from pb.cmd_pb2 import *
from pb.account_pb2 import *

HOST, PORT = "localhost", 2018

if __name__ == "__main__":

    msg = CsLogin()
    msg.name = input("Please input your name:")
    msg.password = input("Please input your password:")

    data = msg.SerializeToString()
    head = struct.pack("!hhh", 6, len(data), CS_CMD_LOGIN)

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(head)
        sock.sendall(data)

        head = sock.recv(6)
        headLen, dataLen, cmd = struct.unpack("!hhh", head)

        if headLen != 6:
            print("Head length is error")
            quit(-1)

        if cmd != SC_CMD_LOGIN:
            print("Logical error")
            quit(-2)

        data = sock.recv(dataLen)
        
        msg = ScLogin()
        msg.ParseFromString(data)

        if msg.res == 0:
            print("Succeed to login")
        else:
            print("Be failed to login")

