# test server
# the server is the listener
# which handles events found by the monitor
# so the monitor is the client

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(("localhost", 9988))
s.listen(1)

def my_function_that_handles_data(data):
    #print('data: ' + str(data))
    data_str = data.decode()
    print('data_str: ' + str(data_str))

while True:
    conn, addr = s.accept()
    data = conn.recv(1024)
    conn.close()
    my_function_that_handles_data(data)