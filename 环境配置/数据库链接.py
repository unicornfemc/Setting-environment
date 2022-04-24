import pymysql

print("================测试是否连通====================")
try:
    conn = pymysql.connect(host='127.0.0.1', user='root',
                           passwd='Beyond09', db='test', port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute('select version()')
    version = cur.fetchone()
    print(version)
    cur.close()
    conn.close()
except Exception:
    print("发生异常")
