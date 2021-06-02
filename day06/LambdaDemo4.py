# 利用 lambda 設計一個 bmi  函數式宣告
# 並求出 170, 60 的 bmi 值

bmiValue = lambda h, w : w / ((h/100) ** 2)
printBmiValue = lambda value : print("bmi: %.2f" % value)
printBmiValue(bmiValue(170, 60))

