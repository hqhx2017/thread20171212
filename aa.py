import time
import _thread

def method(num):
    for i in range(1,num,-1):
        print("子线程"+str(i))


if __name__=="__main__":
    #创建一个新的线程
    _thread.start_new_thread(method,(101,))
    for i in range(1,101,1):
        print("主线程"+str(i))

while True:
    pass