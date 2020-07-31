import pandas as pd
import time
from efficient_apriori import apriori

#读取数据
data=pd.read_csv("订单表.csv",encoding='gbk')

#初始化
transactions=[]
temp_index=0

oders_series=data.set_index('客户ID')['产品名称']
oders_series=oders_series.sort_index()  #客户ID作为index排序

#创建同一ID的集合
for i, v in oders_series.items():
		if i != temp_index:
			temp_set = set()
			temp_index = i
			temp_set.add(v)
			transactions.append(temp_set)
		else:
			temp_set.add(v)

#挖掘频繁项集和关联规则
itemsets, rules = apriori(transactions, min_support=0.1,  min_confidence=0.27)
print('频繁项集：', itemsets)
print('关联规则：', rules)
