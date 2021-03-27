import random
import socket
from socket_stuff import createSocket
import os

def get_img_src(html):
    imgs = html.split("<img")
    all_img_srcs = []
    for one_img in imgs:
        img_src_loc = one_img.find("src")
        first_quote = one_img[img_src_loc:-1].find("\"")
        last_quote = one_img[img_src_loc:-1][first_quote+1:-1].find("\"")
        img_src = one_img[img_src_loc:-1][first_quote+1:last_quote+first_quote+1]
        if img_src != "":
            all_img_srcs.append(img_src)
    return all_img_srcs


def create_img_filename(foldername):
    if not os.path.exists(foldername):
        os.mkdir(foldername) 
    filename = os.path.join(foldername, "img " + str(random.randint(0,100)) + ".jpg")
    if os.path.exists(filename) == True:
        return create_img_filename(foldername)
    return filename


def download_imgs(url, img_list, port, foldername):
    new_img_loc = []
    for img in img_list:
        if img == '':
            pass
        else:
            img_url = url + img
            host_ip = socket.gethostbyname(url)
            address = (host_ip, int(port))
            s = createSocket()
            s.connect(address)
            request = b"GET " + img.encode("utf-8") + b" HTTP/1.1\nHost: "+ url.encode('utf-8') +b"\n\n"
            s.send(request)
            
            buffer = 512
            recieved = s.recv(buffer)
            while b'\r\n\r\n' not in recieved:
                recieved += s.recv(buffer)
            content_info, data = recieved.split(b"\r\n\r\n")
         
            content_info = str(content_info)
            content_length = content_info.find("Content-Length: ")
            image_size = content_info[content_length+len("Content-Length: "):content_length+200].split("\\r\\n")[0]
            total = data
            while not int(image_size) == len(total):  
                data = s.recv(buffer)
                total = total + data
            filename = create_img_filename(foldername)
            with open(filename, "wb") as f:
                f.write(total)
            new_img_loc.append(filename)
    return new_img_loc