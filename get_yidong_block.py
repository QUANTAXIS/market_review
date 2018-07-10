import pandas as pd
import numpy as np
import QUANTAXIS as QA


import datetime

r1=datetime.datetime.now()

# 获取版块
block=QA.QA_fetch_stock_block_adv()
# 获取全市场股票
code=QA.QA_fetch_stock_list_adv().code.tolist()
# 获取全市场股票的1分钟线
min_data=QA.QA_fetch_stock_min_adv(code,'2018-07-01','2018-07-10','1min')
# 获取单个bar大于3%的股票
L=min_data.fast_moving(0.03)

L1=QA.QA_DataStruct_Series(L)
# 查找这些股票所属的版块 其中最多的版块被列出来
res=pd.Series(L1.datetime,index=L1.datetime).apply(lambda x: block.get_code(L1.select_time(x).code).view_block.apply(lambda x: len(x)).sort_values(ascending=False).head(1).index[0])

print(datetime.datetime.now()-r1)

# 保存成csv
res.to_csv('yidongBLock.csv')