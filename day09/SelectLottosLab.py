# 查出 n1 + n2 + ... + n5 = 60
# 有哪幾筆 ?

import sqlite3

conn = sqlite3.connect('demo.db')
cursor = conn.cursor()
#查詢欄位名稱, 利用 TABLE_INFO
cursor.execute('PRAGMA TABLE_INFO("Lotto")')
info = cursor.fetchall()
print(info)
names = [ t[1] for t in info]
print(names)
print("\n---------------------------------------------")
for name in names:
    print(name, end='\t')
print("\n---------------------------------------------")

# 查詢 sql
sql = 'select id, n1, n2, n3, n4, n5, ts from Lotto'
cursor.execute(sql)
rows = cursor.fetchall()
#print(rows)
count = 0
for r in rows:
    #print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
    if (r[1] + r[2] + r[3] + r[4] + r[5]) == 60:
        print('%d\t%d\t%d\t%d\t%d\t%d\t%s' % (r[0], r[1], r[2], r[3], r[4], r[5], r[6]))
        count = count + 1

print("有 %d 筆" % count)


conn.close()
