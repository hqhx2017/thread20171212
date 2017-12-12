import threading
import time
m=500


class MyThread(threading.Thread):
    #定义一个构造方法
    def __init__(self,name,lock):
        threading.Thread.__init__(self)
        self.name=name
        self.lock=lock

    #重写父类的run方法
    def run(self):
        global m
        for i in range(5):
            #获取锁
            self.lock.acquire()
            self.lock.acquire()
            #取钱每次取100
            if m>=100:
                m=m-100
                print(self.name+"取钱100还剩%d"%m);
            #释放锁
            self.lock.release()
            self.lock.release()
            time.sleep(1)
#创建一个锁对象
lock=threading.RLock()

#创建一个线程对象
t1=MyThread("张三",lock)
t2=MyThread("李四",lock)
t3=MyThread("王五",lock)
t4=MyThread("赵六",lock)
t1.start()
t2.start()
t3.start()
t4.start()

