string='我是中国人，人民爱中国'  # 定义一个字符串变量，存储文本信息
s_list=set(string)  # 将字符串转换为集合，去除重复元素
for c in s_list:  # 遍历集合中的元素
    print(c,string.count(c)) 