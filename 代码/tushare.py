import pandas as pd
import tushare as ts
print('df')

df = ts.get_stock_basics()
print(df)
