import socket


mystock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mystock.connect( ('data.pr4e.0rg',80) )