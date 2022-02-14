import socket, sys

try:

    hostname = str(sys.argv[1])

    ip = socket.gethostbyname(hostname)

    print (hostname + ' has an IP of ' + ip)

except:
    print("Something went wrong")
