class Computer():    #创建电脑类
    def __init__(self,type,price,color):   #创建构造函数，定义类变量
        self.type = type                    #类变量品牌
        self.price = price                  #类变量价格
        self.color = color                  #类变量颜色
    def product(self):                      #创建类方法
        if self.type == "微软":               #判断品牌，如果品牌为微软，播报中国工厂制造
            print("中国工厂制造哦")
        elif self.type == "MAC":              #判断品牌，如果品牌为MAC，播报老美的东西
            print("老美的东西")
        elif self.type == "DELL":             #判断品牌，如果品牌为DELL，播报本土品牌
            print("本土品牌")
        else:                                 #判断品牌，如果品牌为其他，播报不知道哪国的
            print("不知道哪国的")


mycomputer = Computer(type="DELL",price=5500,color="黑色")        #实例化自己的电脑
mycomputer.product()                    #实例化方法