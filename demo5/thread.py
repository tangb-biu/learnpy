#!/usr/bin/env python
#coding:utf-8
'''
Created on 2017年5月7日
@author: 唐斌
'''

import time, threading
'''
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %d' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s is ended.' % threading.current_thread().name)
    
print('thread %s is running....' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended' % threading.current_thread().name)
'''
'''
balance = 0
lock = threading.Lock()
def change_it(n):
    global balance
    lock.acquire()
    try:
        balance = balance + n
        balance = balance - n
    finally:
        lock.release()
    
def run_thread(n):
    for i in range(1000000):
        change_it(n)
        
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))

t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
'''

local_school = threading.local()

def process_student():
    std = local_school.student
    print('Hello, %s (in %s)' % (std,threading.current_thread().name))
    
def process_thread(name):
    local_school.student = name
    process_student()
    
t1 = threading.Thread(target=process_thread, args=('Alice',), name="Thread-A")
t2 = threading.Thread(target=process_thread, args=('Bob',), name="Thread-B")
t1.start()
t2.start()
t1.join()
t2.join()