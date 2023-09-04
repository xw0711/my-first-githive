from multiprocessing import Process, Lock
import time, json
# import multiprocessing # Mac电脑
def check():
    with open("db.txt","r") as fr:
        res = json.load(fr)
        return res
def buy(i):
    with open("db.txt", "r") as fr:
        res = json.load(fr)
    time.sleep(1)
    if res['count']>0:
        res['count']-=1
        with open("db.txt", "w") as fw:
            json.dump(res,fw)
            print(f'进程{i}购票成功')
        time.sleep(0.5)
    else:
        print(f'票已受空')
def test(i,lock):
    res = check()
    print(f'还剩{res["count"]}张票')
    lock.acquire() # 锁住
    buy(i)
    lock.release() #释放锁
if __name__=="__main__":
    # multiprocessing.set_start_method("fork") #Mac电脑
    lock=Lock()  # 创建锁
    for i in range(1,5):
        p = Process(target=test,args=(i,lock))
        p.start()