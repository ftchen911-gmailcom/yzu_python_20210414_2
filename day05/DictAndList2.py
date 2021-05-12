e1 = {'name':'John', 'salary': 50000, 'program': ['HTML', 'JS']}
e2 = {'name':'Mary', 'salary': 60000, 'program': ['HTML', 'Python']}
e3 = {'name':'Bob', 'salary': 70000, 'program': ['Java', 'Python', 'C#']}
emps = [e1, e2, e3]
print(len(emps), emps)

# 請求出會 Python 的員工人名, 並將放入到 names = []
sum = 0
name = []
for emp in emps:
    for prg in emp['program']:
        if prg == 'Python':
            name.append(emp['name'])
            print("%s" % emp['name'])
print(name)

