class Plant:   #创建植物类
    def __init__(self,subject,leaves):  #创建构造函数，说明类变量
        self.subject = subject          #类变量科目subject
        self.leaves = leaves            #类变量叶子leaves

    def growup(self):                   #定义共有的生长函数
        print("需要浇水才能长大哦~~")    #打印生长特性

    def workbyleaf(self):               #定义叶子的工作原理函数
        if self.leaves == "绿色":         #增加判断，如果传入的叶子颜色是绿色，就打印绿色叶子的作用
            print("绿色的叶子帮植物做光合作用哦")
        else:                               #如果传入的叶子颜色不是绿色，打印非绿色叶子的作用
            print("这个颜色的叶子我也不知道能干啥呢")

bamboo = Plant("bamboo","绿色")       #实例化竹子，传入竹子叶子颜色为绿色
bamboo.growup()                         #实例化类方法
bamboo.workbyleaf()                     #实例化workbyleaf方法

ziyeli = Plant("rosaceae","红色")        #实例化紫叶李，传入紫叶李叶子颜色为红色
ziyeli.growup()                         #实例化类方法
ziyeli.workbyleaf()                     #实例化workbyleaf方法