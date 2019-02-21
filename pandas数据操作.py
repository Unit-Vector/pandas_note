
# coding: utf-8

# In[1]:


#排序

#sort_index对行或列索引进行排序，默认升序排列
import pandas as pd
ssort=pd.Series(range(5),index=['b','a','d','e','c'])
ssort.sort_index()


# In[2]:


#设置ascending参数将排序改为降序，无论何时缺失值会被放到末尾
ssort.sort_index(ascending=False)


# In[7]:


dfdata={'name':['zhangsan','lisi','wangermazi','zhao','qiang','sun'],
        'subject':['literature','history','ebglish','maths','phtsics','chemist'],
        'score':[98,78,75,86,90,56]}
scoresheet2=pd.DataFrame(dfdata)
scoresheet2.index=[102,101,106,104,103,105]
scoresheet2


# In[9]:


scoresheet2.sort_index()


# In[10]:


#行的顺序按照降序排列
scoresheet2.sort_index(axis=0,ascending=False)


# In[11]:


#列的顺序按照降序排列
scoresheet2.sort_index(axis=1,ascending=True)


# In[18]:


#指定DataFrame的某个列进行排序
scoresheet2.sort_values(by='score',ascending=False)


# In[19]:


#排名

#rank返回每个数的排名,默认选项为average即
#若数的大小相同，则排名相加后除以个数，如下列排序后为（1，2，4，4，9，9，9，10，12，14）4的排名为3和4，则（3+4）/2=3.5
rrank=pd.Series([10,12,9,9,14,4,2,4,9,1])
rrank.rank()


# In[20]:


rrank.rank(ascending=False)


# In[26]:


#选项为first时，按值在原始数据中出现的顺序分配排名
rrank.rank(method='first',ascending=False)


# In[27]:


#选项为max时，取整个相同排名的最大排名
rrank.rank(method='max')


# In[28]:


scoresheet2.rank()


# In[29]:


#运算

#对不同索引的对象进行算数运算，运算时系统按照不同索引自动对齐，存在不同索引时，索引取并集，值为NaN
cs1=pd.Series([1.5,2.5,3,5,1],index=['a','c','d','b','e'])
cs2=pd.Series([10,20,30,50,10,100,20],index=['c','a','e','b','f','g','d'])
cs1+cs2


# In[31]:


import numpy as np
cdf1=pd.DataFrame(np.arange(10).reshape(2,5),columns=list('bcaed'))
cdf2=pd.DataFrame(np.arange(12).reshape(3,4),columns=list('abcd'))
cdf1+cdf2


# In[33]:


#可以使用add,sub(减)，div（除），和mul（乘）等方法将其他dataframe对象传入指定dataframe对象
cdf1.div(cdf2,fill_value=0)


# In[34]:


#函数应用与映射

#ufunc应用于pandas对象Series
reversef=lambda x:-x
reversef(cs2)


# In[35]:


rangef=lambda x:x.max()-x.min()
rangef(cs2)


# In[36]:


#DataFrame对象的apply方法可以将函数应用到各行各列上
rangef(cdf1.add(cdf2,fill_value=0))


# In[37]:


(cdf1.add(cdf2,fill_value=0)).apply(rangef,axis=0)


# In[38]:


(cdf1.add(cdf2,fill_value=0)).apply(rangef,axis=1)


# In[40]:


#可以用applymap方法格式化各个元素
def statistics(x):
    return pd.Series([x.min(),x.max(),x.max()-x.min(),x.mean(),x.count()],index=['min','max','range','mean','N'])
outformat=lambda x:'%.2f' % x
((cdf1.add(cdf2,fill_value=0)).apply(statistics)).applymap(outformat)


# In[43]:


#合并
c1=pd.DataFrame({'Name':{101:'Zhang san',102:'Li si',103:'Wang wu',104:'Zhao liu',105:'Qian qi',106:'Sun ba'},
                 'Subject':{101:'Literature',102:'Hisotry',103:'English',104:'Maths',105:'Physics',106:'Chemics'},
                 'Score':{101:98,102:76,103:84,104:70,105:93,106:83}})
c1


# In[44]:


c2=pd.DataFrame({'Gender':{101:'Male',102:'Male',103:'Male',104:'Female',105:'Female',106:'Male'}})
c2


# In[45]:


#使用concat方法合并两个DataFrame
c=pd.concat([c1,c2],axis=1)
c


# In[46]:


#使用append方法将指定行追加到现有的pandas对象中
c1.append(c2)


# In[47]:


#与以下结果相同
pd.concat([c1,c2],axis=0)


# In[48]:


c3=pd.DataFrame({'Name':{101:'Zhang san',102:'Li si',103:'Wang wu',104:'Zhao liu',105:'Qian qi',106:'Sun ba'},
                 'Gender':{101:'Male',102:'Male',103:'Male',104:'Female',105:'Female',106:'Male'}})
c3


# In[49]:


#使用merge函数按照指定的关键字进行合并
pd.merge(c1,c3,on='Name')


# In[135]:


#分类数据
student_profile=pd.DataFrame({'Name':['Morgan wang','Jackie li','Tom ding','Erric john','Jun Saint','Sui mike','Li rose'],
                             'Gender':[1,0,0,1,0,1,2],
                             'Blood':['A','AB','O','AB','B','O','A'],
                             'Grade':[1,2,3,2,3,1,2],
                             'Height':[175,180,168,170,158,191,173]})
student_profile


# In[136]:


#astype方法将原始数据转化为category类型，然后用cat.category为数据值挂上标签
student_profile['Gender_value']=student_profile['Gender'].astype('category')
student_profile['Gender_value'].cat.categories=['Female','Male','Unconfirmed']
student_profile


# In[144]:


#利用cut函数对数值型数据分段标签          
labels=["{0}-{1}".format(i,i+10) for i in range(160,200,10)]
student_profile['Height_group']=pd.cut(student_profile.Height,range(160,205,10),right=False,labels=labels)
student_profile


# In[146]:


#时间序列

pd.Timestamp('now')


# In[147]:


#利用时间戳创建一个时间序列 Timestamp
dates=[pd.Timestamp('2017-07-05'),pd.Timestamp('2017-07-06'),pd.Timestamp('2017-07-07')]
ts=pd.Series(np.random.randn(3),dates)
ts


# In[148]:


type(ts.index)


# In[150]:


#创建DatetimeIndex实例对象索引的方式还可以通过 date_range 函数实现
dates=pd.date_range('2017-07-05','2017-07-07')
tsdr=pd.Series(np.random.randn(3),dates)
tsdr


# In[151]:


type(tsdr.index)


# In[152]:


#将类Period实例化也可以得到以Period实例对象为索引的时间序列
dates=[pd.Period('2017-07-05'),pd.Period('2017-07-06'),pd.Period('2017-07-07')]
tsp=pd.Series(np.random.rand(3),dates)
tsp


# In[153]:


type(tsp.index)


# In[157]:


#data_range 
#pd.data_range(start=None,end=None, periods=None,freq='D',tz=None,normalize=False,name=None,closed=None)
#periods指定时间日期的个数
pd.date_range(start='2018/07/07',periods=3,freq='M')


# In[158]:


#freq除了可用来指定时间日期的频率，也可以指定生成时序时的偏移量
pd.date_range('2017/07/07','2018/07/07',freq='BMS')


# In[159]:


pd.date_range('2017/07/07',periods=10,freq='1D2h20min')


# In[160]:


pd.date_range('2017/07/07','2018/01/22',freq='W-WED')


# In[162]:


#自定义时间偏移量
ts_offset=pd.tseries.offsets.Week(1)+pd.tseries.offsets.Hour(8)
ts_offset


# In[163]:


pd.date_range('2017/07/07',periods=10,freq=ts_offset)


# In[165]:


#缺失数据

scoresheet=pd.DataFrame({'Name':['Christoph','Morgan','Mickel','Jones'],
                        'Economics':[89,97,56,82],
                        'Statistics':[98,93,76,85]})
scoresheet


# In[166]:


scoresheet['Datamining']=[79,np.nan,None,89]
scoresheet.loc[[1,3],['Name']]=[np.nan,None]
scoresheet


# In[169]:


#缺失值在默认情况下不参与运算及数据分析过程
print(scoresheet['Datamining'].mean())
print(scoresheet['Datamining'].mean()==(79+89)/2)


# In[175]:


scoresheet['Exam_Date']=pd.date_range('20170707',periods=4)
scoresheet['Exam_Date']


# In[176]:


#时间戳默认缺失值是NaT
scoresheet.loc[[2,3],['Exam_Date']]=np.nan
scoresheet


# In[177]:


#对于空值可以使用isnull（）notnull判定
scoresheet.isnull()


# In[178]:


#缺失数的填充 fillna（） 

#**时间序列的时间起点为1970-01-01
scoresheet.fillna(0)


# In[179]:


scoresheet['Name'].fillna('miassing')


# In[180]:


#pad关键字（或ffill）可以使用缺失值前的值进行填充
scoresheet.fillna(method='pad')


# In[181]:


#backfill（或bfill）可以使用缺失值后的值进行填充,若后面没有可供填充的非缺失值，则保持为空
scoresheet.fillna(method='bfill')


# In[182]:


scoresheet.bfill() #相当于scoresheet.fillna(method='bfill')


# In[183]:


scoresheet.ffill(limit=1)#当有连续缺失值时，只填充第一个缺失值，不做连续


# In[184]:


#缺失值可以以相应函数运算结果填充
scoresheet['Datamining'].fillna(scoresheet['Datamining'].mean())


# In[185]:


#清洗数据（直接对含有缺失值的数据进行删除） dropna

scoresheet.dropna(axis=0) #删除所有缺失值的行


# In[187]:


scoresheet.dropna(how='any',axis=1) #删除含有任何缺失值的列


# In[189]:


scoresheet.loc[[0],['Exam_Date']]=np.nan
scoresheet


# In[194]:


scoresheet.dropna(how='any',thresh=2,axis=1)

#参数how可以指定any和all，any表示删除含有任意缺失值的行和列，all表示删除全部数据均是缺失值的行或列，
#参数thresh表示删除非缺失数据量小于参数值的行或列


# In[195]:


#缺失数据插值 interpolate
#利用已有数据对数值型缺失值进行估计，并用估计结果替换缺失值

scoresheet.interpolate(method='linear') #对scoresheet进行线性插值


# In[196]:


scoresheet.interpolate(method='polynomial',order=1)

