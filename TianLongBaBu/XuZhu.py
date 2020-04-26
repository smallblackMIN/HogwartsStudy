from TianLongBaBu.TongLao import TongLao   #导入TongLao类

class XuZhu(TongLao):   #继承TongLao
    def read(self):     #没写init方法，表示不重写，直接复用父类构造方法，然后新增子类方法read
        print("罪过罪过")       #打印read方法内容


xuzhu = XuZhu(1000,300)         #实例化虚竹
xuzhu.read()                    #实例化子类方法