# 导入需要的库
import mariadb
import pandas as pd
# 建立数据库连接
conn = mariadb.connect(host='192.168.31.167', user='root2',
                       password="Beyond09", database='test')
# 建立游标
cur = conn.cursor()
# 输入SQL命令
sql = "select * from qwe"
# 执行SQL
cur.execute(sql)
# 遍历数据表并打印
for r in cur:
    print(r)
# 关闭数据库
cur.close()
# 关闭数据库连接
conn.close()
