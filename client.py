import socket
import sys
import time
import os
import random
from find_img import get_img_src, download_imgs
from socket_stuff import createSocket



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


    try:
        port = request[2]
    except IndexError:
        port = 80
    url = request[1]
    if request[0] == 'GET':
        getRequest(host_ip, port, url)
    
    if request[0] == 'HEAD':
        headRequest(host_ip, port, url)

    if request[0] == 'POST':
        postRequest()
    
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
    while b"</html>" not in (recieved):

        total = total + recieved
        recieved = s.recv(buffer)
        
    total = total + recieved
    head, html = find_body(total.decode('unicode_escape'))
    print(head)
    foldername = create_filename(url)
    os.mkdir(foldername)
    
    all_img_src = get_img_src(html)
    new_img_loc = download_imgs(url, all_img_src, port, foldername)

    for one_src in all_img_src:
        html = html.replace(one_src, new_img_loc[all_img_src.index(one_src)].split("\\")[-1])
        

    with open(os.path.join(foldername, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    



def headRequest(host_ip, port, url):
    address = (host_ip, int(port))
    s.connect(address)
    request = b"HEAD / HTTP/1.1\nHost: "+ url.encode('utf-8') + b"\n\n"
    s.send(request)
    buffer = 512
    recieved = s.recv(buffer)
    total = b''
    while "\r\n\r\n" not in (recieved).decode("utf-8")[-10:]:
       
        total = total + recieved
        recieved = s.recv(buffer)
        
    total = total + recieved
    print(total.decode("utf-8"))




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
    return filename

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
    arguments = sys.argv[1], sys.argv[2], sys.argv[3] #input('enter url').split(' ') #
    # while True:
        # request = input("HttpCommand URI Port: ")
    parseInput(arguments)
    #time.sleep(1)
        #Server disconnect when I type 'POST Disconnect!'
        #if not s.recv(HEADER).decode('utf-8'):
         #   break
