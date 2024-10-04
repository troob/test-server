# test server
# the server is the listener
# which handles events found by the monitor
# so the monitor is the client

import socket


def my_function_that_handles_data(data):
    print('\n===Handle Data from Client===\n')
    data_str = data.decode()
    print('data_str: ' + str(data_str))


host = 'localhost' # Standard loopback interface address (localhost)
port = 9988 # Port to listen on (non-privileged ports are > 1023)

# Echo Server
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host, port))
    s.listen(1)

    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break

            # echo data back to server
            conn.sendall(data)
            #my_function_that_handles_data(data)

    