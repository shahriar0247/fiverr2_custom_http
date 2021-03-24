import socket
import sys


def createSocket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")
    except socket.error as err:
        print("socket creation failed with error %s" % (err))
    return s


def parseInput(request):

    request = request.split(' ')

    if request == DISCONNECTMSG:
        s.close()
        return

    try:
        host_ip = socket.gethostbyname(request[1])
    except socket.gaierror:
        # this means could not resolve the host
        print("there was an error resolving the host")
        sys.exit()
    print(len(request))

    try:
        port = request[2]
    except IndexError:
        port = 80

    if request[0] == 'GET':
        getRequest(host_ip, port)

    if request[0] == 'POST':
        postRequest()

#this is wrong, not http protocol
def getRequest(host_ip, port):
    address = (host_ip, port)
    s.connect(address)
    print("the socket has successfully been connected")

#this is wrong not http protocol
def postRequest():
    msg = input('Provide a message to the server: ')
    message = msg.encode('utf-8')  # Should probably check with server/client which encoding to use here dynamically
    s.send(message)




if __name__ == '__main__':
    s = createSocket()
    HEADER = 64
    SERVER = socket.gethostbyname(socket.gethostname())
    DISCONNECTMSG = 'DISCONNECT!'
    while True:
        request = input("HttpCommand URI Port: ")
        parseInput(request)
        #Server disconnect when I type 'POST Disconnect!'
        #if not s.recv(HEADER).decode('utf-8'):
         #   break
