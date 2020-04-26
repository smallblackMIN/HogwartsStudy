class TongLao:                         #创建童姥类
    def __init__(self,hp,power):        #构造函数，说明类属性
        self.hp = hp                    #类属性血量
        self.power = power              #类属性攻击值
    def see_people(self,name):          #定义类方法see_people
        if name == "WYZ":               #判断看到的人是WYZ
            print("师弟！！！")          #大呼师弟
        elif name == "李秋水":           #判断看到的人是李秋水
            print("呸，贱人")            #说呸，贱人
        elif name == "丁春秋":             #判断看到的人丁春秋
            print("叛徒！我杀了你")        #说叛徒我杀了你
        else:                               #判断看到的是其他人
            print("路人与我何干")             #说路人与我何干
    def fight_zms(self,enemy_hp,enemy_power):  #定义类方法fight_zms，并且声明需要传入敌人血量和攻击值
        hp = self.hp/2                          #将类变量中即童姥本人血量除二
        power = self.power * 10                 #将类变量中即童姥本人攻击值乘以10
        if (hp - enemy_power) > (enemy_hp - power):     #一轮打斗后，童姥本人血量为减去敌人攻击值，敌人血量为减去童姥攻击值，比较两者，如果童姥打斗后血量大于敌人
            print("哈哈哈，我赢了")                        #打印我赢了
        elif (hp - enemy_power) < (enemy_hp - power):       #如果一轮打斗后，童姥打斗后血量小于敌人
            print("再来一局")                               #打印再来一局
        else:                                               #如果一轮打斗后，血量相等
            print("没想到，你还有两下子")                     #夸赞对方还有两下子

tonglao = TongLao(1000,200)                         #实例化童姥
tonglao.see_people("路人甲")                           #实例化see_people方法
tonglao.fight_zms(5000,100)                         #实例化fight_zms方法
