class Dog:       #创建狗类
    def __init__(self,name,color):  #将共有属性初始化，方便实例化的时候对类变量进行赋值
        self.name = name            #类变量name
        self.color = color          #类变量color
    def bark(self):                 #定义狗狗共有的功能bark
        print(self.name,"喜欢汪汪汪~~~")   #打印xx狗喜欢汪汪汪
    def play(self):                  #定义狗狗共有的功能paly
        print(self.name,"爱玩丢球")     #打印xx狗爱玩丢球

mindog = Dog("小花","白色")    #实例化狗对象，并传入名字和颜色
mindog.bark()           #调用bark方法打印这只狗的特性
mindog.play()           #调用play方法打印这只狗的特性
