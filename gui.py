from tkinter import *
import socket
import threading

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLable = Label(self, text='hello, world')
        self.conButton = Button(self, text='ClientConnect', command=self.connect)
        self.quitButton = Button(self, text='quit', command=self.quit)
        self.helloLable.pack()
        self.conButton.pack()
        self.quitButton.pack()

    def connect(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 建立连接:
        s.connect(('127.0.0.1', 9999))
        # 接收欢迎消息:
        print(s.recv(1024).decode('utf-8'))
        for data in [b'Michael', b'Tracy', b'Sarah']:
            # 发送数据:
            s.send(data)
            print(s.recv(1024).decode('utf-8'))
        s.send(b'exit')
        s.close()

    def client_connect(self):
        # ipv4
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 链接
        s.connect(('www.sina.com.cn', 80))
        # get
        s.send(b'GET / HTTP/1.1\r\nHost: www.sina.com.cn\r\nConnection: close\r\n\r\n')

        #接收数据
        buffer = []
        while True:
            #每次只获取1k的数据
            d = s.recv(1024)
            print('get Data: ',d)
            # buffer.append(d) if d else break
            if d:
                buffer.append(d)
            else:
                break

        s.close()
        data = b''.join(buffer)

        header, html = data.split(b'\r\n\r\n', 1)
        print(header.decode('utf-8'))
        # 把接收的数据写入文件:
        with open('/Users/shitakusei/Desktop/sina.html', 'wb') as f:
            f.write(html)


# def server_connect():

#     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     s.bind(('127.0.0.1', 9999))
#     s.listen(5)
#     print('Waiting for connection...')

#     while True:
#         sock, address = s.accept()
#         t = threading.Thread(target=tcp_link, args=(sock, address))
#         t.start()

# def tcp_link(sock, address):
#     print('accept: %s'%address)
#     print('comein')
#     while True:
#         data = sock.recv(1024)
#         if not date or data.decode('utf-8') == 'exit':
#             break

#     sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
#     sock.close()
#     print('Connection from %s:%s closed.' % addr)



app = Application()
app.master.title="fuck"
app.mainloop()

