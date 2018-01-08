# -*- coding: utf-8 -*-

'hello module'

__author__ = 'shituocheng'

from types import MethodType

import sys
import types
from multiprocessing import Process, Queue
import os, time, random
import threading
import socket

def test():
    args = sys.argv

    # raise TypeError('fuck')
    if len(args) == 1:
        print(args)
    elif len(args) == 2:
        print(args, args[1])
    else: 
        print('too much args')

if __name__ == '__main__':
    test()

class Cat(object):
    def __init__(self, color, size):
        self.__color = color
        self.__size = size

    def get_color(self):
        return self.__color

    def get_size(self):
        return self.__size

    def set_color(self, color):
        if not isinstance(color, (str)):
            raise TypeError('cannot string')
        self.__color = color

    def set_size(self, size):
        if not isinstance(size, (str, int, float)):
            raise TypeError('type error')
        self.__size = size

class Student(object):
    
    @property
    def name(self):
        return self.__name

    @property
    def gender(self):
        return self.__gender

    @name.setter
    def name(self, name):
        if not isinstance(name, (str)):
            raise TypeError('string error')

        self.__name = name

    @gender.setter
    def gender(self, gender):
        if gender not in ('man', 'female'):
            raise ValueError('unvalid value')

        self.__gender = gender


class SmallCat(Cat):
    pass

s = Student()
print(s)
# small = SmallCat('red', 'small')
# print(isinstance(small, (Cat, str)))
# print(dir(small))

class Animal(object):
    pass

# 大类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class Runnable(object):
    def run(self):
        print('running')

class Flyable(object):
    def fly(self):
        print('flying')


class Lit(object):
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 1000:
            raise StopIteration()

        return self.a

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值


# 写数据进程执行的代码:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

def loop():
    print(threading.current_thread().name)

thread = threading.Thread(target=loop, name='subthreading')
thread.start()
thread.join()
print(threading.current_thread().name)

# 假定这是你的银行存款:
balance = 0
lock = threading.Lock()

def change_it(n):
    # 先存后取，结果应该为0:
    global balance
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for i in range(100000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()

t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
 
local_school = threading.local()
def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    local_school.student = name
    process_student()

def server_connect():

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(('127.0.0.1', 9999))
    s.listen(5)
    print('Waiting for connection...')

    while True:
        sock, address = s.accept()
        t = threading.Thread(target=tcp_link, args=(sock, address))
        t.start()

def tcp_link(sock, address):
    print('accept: %s'%address)
    print('comein')
    while True:
        data = sock.recv(1024)
        if not date or data.decode('utf-8') == 'exit':
            break

    sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

if __name__ == '__main__':
    server_connect()




