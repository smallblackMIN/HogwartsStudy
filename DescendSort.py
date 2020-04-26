def DescendSort(list):          #创建非递减顺序排序函数
    list1 =sorted([i**2 for i in list])  #列表推导式，[i**2 for i in list]表示对list中的数平方，sorted()表示对列表推导出来的结果进行排序
    print(list1)                        #打印list平方后，排序结果

DescendSort(list=[-4,-1,0,3,10])     #调用函数，传入list[-4,-1,0,3,10]
DescendSort(list=[-7,-3,2,3,11])     #调用函数，传入list[-7,-3,2,3,11]