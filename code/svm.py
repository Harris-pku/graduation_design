import csv
import jieba
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn import metrics
from sklearn.grid_search import GridSearchCV
from sklearn.model_selection import train_test_split

#导入正例负例数据
def load_datas(bid):
    Pfilename = 'result'+str(bid)+'positive.csv'
    df_P = pd.DataFrame(pd.read_csv(Pfilename, encoding='utf-8'))
    Nfilename = 'result'+str(bid)+'negative.csv'
    df_N = pd.DataFrame(pd.read_csv(Nfilename, encoding='utf-8'))
    #为正例打标签1
    df_P = df_P[['name']]
    df_P['label'] = 1
    #为负例打标签0
    df_N = df_N[['name']]
    df_N['label'] = 0
    #将正例和负例合并成一个大表
    df_P_part = df_P
    df_N_part = df_N
    pd_merge = pd.concat([df_P_part,df_N_part])
    return pd_merge
    
def randSplit(dataSet,n):
    dataSet = {"name": pd.Series(dataSet["name"].values),
            "label": pd.Series(dataSet["label"].values)}
    datas = pd.DataFrame(dataSet)
    data_rdm = datas.sample(n) 
    return data_rdm
    
# 过滤停用词
def filter_stop_word(lines,sentence):
    wordlst = []
    for word in sentence.split(' '):
        if word in lines:
            continue
        else:
            wordlst.append(word)
    return ' '.join(wordlst)

datas['Nfenci'] = datas['fenci'].apply(lambda i: filter_stop_word(lines,i))

def predict_SVM(xtrain, ytrain, xvalid):
    text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', SVC(C=0.99, kernel = 'linear'))])
    text_clf = text_clf.fit(xtrain, ytrain.values)
    return text_clf
    
    
if __name__=='__main__':
    #导入数据
    datas = load_datas('1wet')
    #随机生成数据集
    dataSet = datas
    datas = randSplit(dataSet)
    y = datas['label']
    
    jieba.set_dictionary('dict.txt')
    
    # datas['name'] = datas['name'].apply(lambda i: filter_number_english(i))
    datas['fenci'] = datas['name'].apply(lambda i:' '.join(jieba.cut(i)))
    
    #导入停用词
    filename='stopwdlst.txt'
    with open(filename,'r') as file:
        lines = file.read().splitlines()
        
    #将数据分成训练和验证集
    xtrain, xvalid, ytrain, yvalid = train_test_split(datas.Nfenci.values, y, 
                                                      stratify=y, 
                                                      random_state=42, 
                                                      test_size=0.2, shuffle=True)
                                
    # 计算权重
    vectorizer = CountVectorizer()
    tfidftransformer = TfidfTransformer()
    tfidf = tfidftransformer.fit_transform(vectorizer.fit_transform(xtrain))  # 先转换成词频矩阵，再计算TFIDF值
    #print(tfidf.shape)
    
    test_data = pd.DataFrame(xvalid)
    test_data['label'] = yvalid.tolist()
    text_clf = predict_SVM(xtrain, ytrain, xvalid)
    test_data['predicted_label_SVM']=test_data[0].apply(lambda i : text_clf.predict([i])[0])
    
    total = test_data['label'].count()
    correct = test_data[test_data['label'] == test_data['predicted_label_SVM']]['label'].count()
    print('总数为：%s，准确数为：%s，准确率为：%s'%(total,correct, correct / total))
    
    test_data.to_csv('1wet.csv',encoding='gbk')
