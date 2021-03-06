file = open('salary.txt', 'r', encoding='UTF-8')
rows = file.readlines()
# 進行資料結構化的整理
# [{'name': John, 'salary': 45000},{'name': Mary, 'salary': 55000} ... ]
employees = []
for row in rows:
    data = row.split(',')
    name = data[0]  # 員工姓名
    salary = int(data[1].strip('\n'))  # 員工薪資
    employee = {'name': name, 'salary': salary}  #dict 字典格式
    employees.append(employee)

print(employees)


#求薪資總合與平均
sum = 0
for employee in employees:
    sum = sum + employee['salary']
avg = sum / len(employees)

print("薪資總合:", sum)
print("薪資平均:", avg)

# 請問最高/低薪的人名是 ?
emp_max = max(employees, key=lambda e: e['salary'])
emp_min = min(employees, key=lambda e: e['salary'])
print(emp_max, emp_max['name'])
print(emp_min, emp_min['name'])

#max = 0
#index = 0
#for employee in employees:
    #print(employee['salary'])
#     if int(employee['salary']) > max：
#         max = employee['salary']
#         index = index + 1
#
# print("最高薪的人是:", employees[index][0])

