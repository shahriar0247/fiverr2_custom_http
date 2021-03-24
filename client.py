import socket
import sys
import time
import os
import random

def createSocket():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket successfully created")
    except socket.error as err:
        print("socket creation failed with error %s" % (err))
    return s


def parseInput(request):

    

    if request[0] == DISCONNECTMSG:
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
    url = request[1]
    if request[0] == 'GET':
        getRequest(host_ip, port, url)

    if request[0] == 'POST':
        postRequest()

#this is wrong, not http protocol
def getRequest(host_ip, port, url):
    address = (host_ip, int(port))
    s.connect(address)
    request = b"GET / HTTP/1.1\nHost: "+ url.encode('utf-8') + b"\n\n"
    s.send(request)
    # result = s.recv(1024)
    # total = result
    # while (len(result) > 0):
    #     amount_left = len(result) - len(total)
    #     result = s.recv(amount_left)
    #     total = total + result
    #     if result == b'':
    #         break
    
    buffer = 512
    recieved = s.recv(buffer)
    total = b''
    while "</html>" not in (recieved).decode("utf-8")[-20:]:
        print(len(recieved))
        total = total + recieved
        recieved = s.recv(buffer)
        
    total = total + recieved
    head, html = find_body(total.decode("utf-8"))
    filename = create_filename(url)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(html)
    
    print("Saved html in %s" % filename)

def get_images_url():
    import re                       # use regexp
    r = re.compile("<img.>") # constructs the search machinery
    res = r.search(original_string) # search
    print (res.group(0))      

def find_body(total):
    split_text = ["<!doctype", "<!DOCTYPE", "<html","<HTML"]
    for a in split_text:
        try:
            total_split = total.split(a)
            total_split[1] = a + total_split[1]
            break
        except:
            pass
    return total_split[0], total_split[1]

def create_filename(params):
    location = "html"
    if not os.path.exists(location):
        os.mkdir(location) 
    filename = os.path.join(location, params)
    while os.path.exists(filename) == True:
        filename = filename + " " + str(random.randint(0,100))
    return filename + ".html"

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
    arguments = sys.argv[1], sys.argv[2] ,sys.argv[3]
    # while True:
        # request = input("HttpCommand URI Port: ")
    parseInput(arguments)
    #time.sleep(1)
        #Server disconnect when I type 'POST Disconnect!'
        #if not s.recv(HEADER).decode('utf-8'):
         #   break
