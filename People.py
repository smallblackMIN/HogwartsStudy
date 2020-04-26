class People():  #创建人类
    def __init__(self,sex):  #创建构造函数，增加类变量
        self.sex = sex       #类变量性别
    def eat(self):          #创建吃的动作
        print("一日三餐都得吃，每个城市的人都喜欢不同的食物")   #打印吃的内容
    def study(self):        #创建学习的动作
        print("从九年制义务教育开始学习呀")      #打印学习的内容

me = People("女")        #实例化People类
me.eat()                #实例化吃函数
me.study()              #实例化学习的动作