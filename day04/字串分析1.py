str = ' she sell sea shell on the sea shore '
print(str)
str = str.strip()  # 除去左右空白
str = str.lstrip()  # 去除左邊空白
str = str.rstrip()  # 除去右邊空白
print('字串長度:', len(str))
print('有幾個s:', str.count('s'))
print('有無 on 這個字的位置:', str.find('on'))
print('有無 on 這個字:', str.find('on') != -1)
print('有無 off 這個字的位置:', str.find('off'))
print('有無 off 這個字:', str.find('off') != -1)
print('有沒有 sea 這個字:', '有' if str.find('sea') >= 0 else '沒有')
print('有沒有 land 這個字:', '有' if str.find('land') >= 0 else '沒有')
print('有幾個單字:', str.count(' ')+1)
#  是否都是英文字(a ~ z, A ~ Z)
print('是否都是英文字:', str.replace(' ','').isalpha())  # 小技巧: 先利用 replace 將中間的空白去除
print(str[2])
print(str[0:3])  # 取出0~3位置的字串(不含3)
path = r'C:\temp\nba\score.py'  # r 不解釋特殊碼, 例如 \t, \n 等等
print('路徑位置:', path)