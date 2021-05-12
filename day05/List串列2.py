import random as r

scores = [100, -10, -20, 90, -80, 999]

for x in scores:
    if x < 0:
        print(x)
    if x > 100:
        print(x)

'''
error_score = scores.pop(1)
print(error_score, scores)
error_score = scores.pop(3)
print(error_score, scores)
'''

# 利用 pop() 將不合法的分數挑出
'''
for (idx, value) in enumerate(scores):
    if value < 0:
        error_score = scores.pop(idx)
        print(error_score, scores)
    if value > 100:
        error_score = scores.pop(idx)
        print(error_score, scores)
'''

'''
# 利用 pop() 將不合法的分數挑出_2
for s in scores:
    if s < 0 or s > 100:
        error_score = scores.pop(scores.index(s))
        print("不合法分數:", error_score)
'''

'''
# 利用 pop() 將不合法的分數挑出_3
error_scores = []
for s in scores:
    if s < 0 or s > 100:
        error_scores.append(s)

print(scores)
print(error_scores)

for e in error_scores:
    scores.pop[scores.index(e)]

print(scores)
'''

'''
# 利用 pop() 將不合法的分數挑出_4
error_scores = []
for s in scores:
    if s < 0 or s > 100:
        error_scores.append(s)

print(scores)
print(error_scores)
for e in error_scores:
    scores.pop(scores.index(e))

print(scores)
'''

# 反轉
scores = [1, 7, 3, 5]
scores.reverse()
print(scores)

# 排序
scores.sort()
print(scores)

# 洗牌 (請先 import random as r)
r.shuffle(scores)
print(scores)