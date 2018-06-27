
# coding: utf-8

# In[274]:


import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


# In[275]:


# Khai báo các file cần load lên (thuộc tập train)
fileList = ["giaoduc" + str(i) + ".txt" for i in range(50)]
fileList = fileList + ["chinhtri" + str(i) + ".txt" for i in range(50)]
fileList = fileList + ["phapluat" + str(i) + ".txt" for i in range(50)]
fileList = fileList + ["suckhoe" + str(i) + ".txt" for i in range(50)]

# Khai báo các file cần load lên (thuộc tập test)
fileList = fileList + ["giaoduc" + str(i) + ".txt" for i in range(50,60)]
fileList = fileList + ["chinhtri" + str(i) + ".txt" for i in range(50,60)]
fileList = fileList + ["phapluat" + str(i) + ".txt" for i in range(50,60)]
fileList = fileList + ["suckhoe" + str(i) + ".txt" for i in range(50,70)]

X = TfidfVectorizer(input='filename').fit_transform(fileList).toarray()

# 200 phần tử đầu thuộc tập train
X_train = X[:200]
# 50 phần từ sau thuộc tập test
X_test = X[200:250]


# In[276]:


Y_train = []
Y_test = []

# Tạo vector chứa nhãn của tập train
for i in range(0,200):
    if (i<50):
        Y_train.append(0) 
    elif (i<100):
        Y_train.append(1)
    elif (i<150):
        Y_train.append(2)
    else:
        Y_train.append(3)
        
# Tạo vector chứa nhãn đúng của tập test, dùng để so sánh với kết quả predict        
for i in range(0,50):
    if (i<10):
        Y_test.append(0) 
    elif (i<20):
        Y_test.append(1)
    elif (i<30):
        Y_test.append(2)
    else:
        Y_test.append(3)


# In[277]:


neigh = KNeighborsClassifier(n_neighbors=5)
print(X_train.size)
print(Y_train)
neigh.fit(X_train,Y_train)


# In[278]:


# Predict kết quả
Y_predict = neigh.predict(X_test)

# So sánh để tính độ chính xác
accuracy_score(Y_predict, Y_test)

