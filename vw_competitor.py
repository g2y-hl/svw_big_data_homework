from sklearn.cluster import KMeans
from sklearn import preprocessing
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, ward
from sklearn.cluster import KMeans, AgglomerativeClustering
import matplotlib.pyplot as plt

#读取数据
data=pd.read_csv('CarPrice_Assignment.csv')
data_new=data.drop(["CarName","car_ID","citympg","highwaympg"],axis=1)

#字符串转化为数字
le=preprocessing.LabelEncoder()
columns=['fueltype','aspiration','doornumber','carbody','drivewheel','enginelocation','enginetype','cylindernumber','fuelsystem']
for column in columns:
    data_new[column]=le.fit_transform(data_new[column])

# 规范化到 [0,1] 空间
min_max_scaler=preprocessing.MinMaxScaler()
data_new=min_max_scaler.fit_transform(data_new)
pd.DataFrame(data_new).to_csv('temp2.csv', index=False)


#主成分分析
pca_sk=PCA(n_components=4)
data_new=pca_sk.fit_transform(data_new)


sse = []
for k in range(1, 20):
	# kmeans算法
	kmeans = KMeans(n_clusters=k)
	kmeans.fit(data_new)
	# 计算inertia簇内误差平方和
	sse.append(kmeans.inertia_)
x = range(1, 20)
plt.xlabel('K')
plt.ylabel('SSE')
plt.plot(x, sse, 'o-')
plt.show()

#k=3分类结果
kmeans = KMeans(n_clusters=5)
kmeans.fit(data_new)
predict_y = kmeans.predict(data_new)
# 合并聚类结果，插入到原数据中
result = pd.concat((data,pd.DataFrame(predict_y)),axis=1)
result.rename({0:u'聚类结果'},axis=1,inplace=True)
print(result)
result.to_csv("car_data.csv",index=False)



