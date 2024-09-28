grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
a = [sum(grades[0])/len(grades[0]),sum(grades[1])/len(grades[1]),sum(grades[2])/len(grades[2]),sum(grades[3])/len(grades[3]),
     sum(grades[4])/len(grades[4])]
b = sorted(students)
print(dict(zip(b,a)))

s = []
for i in grades:
    c =  sum(i)/len(i)
    s.append(c)
print(dict(zip(b,s)))
# avg =[sum(sublist) for sublist in grades]
# average = s / len(grades[0:4])
# print(average)
# for i in range(s):
#     grades.append(int(len(grades)))
#     s = s + grades[i]
# print(s)
# # average = result / len(grades)
