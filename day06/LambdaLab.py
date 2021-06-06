'''
回家作業 (利用 lambda)
id = A123456789
第二碼 sex = id[1] ( 1: 男生, 2: 女生)
第三碼 area = id[2] ( 0~5: 台灣, 6: 外國人, 7:無戶籍, 8: 港澳, 9: 大陸)
印出: 台灣男
'''

#id = 'A123456789'   # 台灣男
#id = 'A293456789'   # 大陸女
#id = 'A163456789'   # 外國男
id = 'A283456789'   # 港澳女

#print(id[1], id[2])
#print(id, "是", "台灣男")

sex = int(id[1])
area = int(id[2])
#print(sex, type(sex))
#sex_error = lambda : print("性別錯誤")

# sex_info = {1: lambda : print("男"), 2: lambda : print("女")}
# sex_info.get(sex)()

area_info = {
                0: lambda sex: print("台灣", "男" if sex == 1 else "女"),
                1: lambda sex: print("台灣", "男" if sex == 1 else "女"),
                2: lambda sex: print("台灣", "男" if sex == 1 else "女"),
                3: lambda sex: print("台灣", "男" if sex == 1 else "女"),
                4: lambda sex: print("台灣", "男" if sex == 1 else "女"),
                5: lambda sex: print("台灣", "男" if sex == 1 else "女"),
                6: lambda sex: print("外國人", "男" if sex == 1 else "女"),
                7: lambda sex: print("無戶籍", "男" if sex == 1 else "女"),
                8: lambda sex: print("港澳", "男" if sex == 1 else "女"),
                9: lambda sex: print("大陸", "男" if sex == 1 else "女")
            }
area_info.get(area)(sex)




