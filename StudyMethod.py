class StudyMethod():   #创建学习方式类
    def __init__(self,subject):     #创建构造方法，定义学科
        self.subject = subject
    def method(self):           #创建类方法
        if self.subject == "语文":  #判断如果学科是语文
            print("需要多读书积累知识，语文才能学得好")  #打印语文的学习方法
        elif self.subject == "数学": #判断如果学科是数学
            print("需要多做题进行练习")      #打印数学的学习方法
        elif self.subject == "英文": #判断如果学科是英文
            print("需要多背单词，练口语")     #打印英文的学习方法
        else:   #判断其他学科
            print("认真听课，经常和老师请教")   #打印其他学科的学习方法

mathMethod = StudyMethod("数学")  #实例化学习方式类
mathMethod.method()     #调用类方法