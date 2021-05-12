# 數組: List(元素可重覆), set(元素不可重覆), dict(key/value)
scores = [100, 90, 80]  # List
scores.append(70)
print(scores)
print(scores[1])  # 取得維度=1的資料(維度是從0開始)
print(len(scores))  # 取得元素個數
print(scores.index(80))  # 取得某元素的維度值, 如果有兩個 80, 就找第一個找到的.
print(max(scores), min(scores))  # 取得元素最大最小值
#  走訪每一個元素
for x in scores:
    print(x)
#  走訪每一個元素(含維度值)
for (idx, value) in enumerate(scores):
    print(idx, value)

