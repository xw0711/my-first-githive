from multiprocessing import Process
import time, json
def search(i):
    time.sleep(1)
    dic = json.load(open('db.txt'))
    print('子进程%s查看剩余票数%s'%(i,dic['count']))
def get():
    dic = json.load(open('db.txt'))
    time.sleep(1) # 模拟读数据的网络延迟
    if dic['count']>0:
        dic['count']-=1
        time.sleep(0.2) # 模拟写数据的延迟
        json.dump(dic,open('db.txt','w'))
        print('购票成功')
def task(i):
    search(i)
    get()
if __name__=="__main__":
    for i in range(1,5):
        p = Process(target=task,args=(i,))
        p.start()
        # p.join() 阻塞，则进程按照顺序执行