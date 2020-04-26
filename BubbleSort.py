def bubblesort(list):#创建冒泡函数
    for i in range(len(list)-1): #设定循环次数
        for j in range(len(list)-1-i):#设定对比次数
            if list[j] > list[j+1]:#比较列表中相邻两个数的大小
                list[j],list[j+1] = list[j+1],list[j] #如果左边大于右边，就交换两个数的位置
    return list #返回冒泡后的list

list=[3,2,1,4,5,6,0,9]  #创建一个未排序的列表
print(bubblesort(list))  #将列表通过冒泡排序后打印出来


