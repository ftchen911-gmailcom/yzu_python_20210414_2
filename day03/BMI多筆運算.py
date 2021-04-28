import math
'''
    170, 50
    180, 70
    160, 60
'''
def printBMI(h, w):
    bmi = w / math.pow(h/100, 2)
    print("h= %.1f w=%.1f bmi=%.2f" % (h, w, bmi))
    #result = "過重" if bmi > 23 else "過輕" if bmi <= 18 else "正常"
    result = "過輕"
    if 18 < bmi <= 23:
        result = "正常"
    elif bmi > 23:
        result = "過重"
    print("h= %.1f w=%.1f bmi=%.2f result=%s" % (h, w, bmi, result))
    '''
    if bmi > 23:
        print("過胖")
    elif bmi <= 18:
        print("過輕")
    else:
        print("正常")
    '''


printBMI(170, 50)
printBMI(180, 70)
printBMI(160, 60)

