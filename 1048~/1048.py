## 실패
#TestCase = int(input())
#for i in range(TestCase):
#    student = []
#    AP_Dorm = []
#    cnt_student = 0
#    Dorm, AP = map(int, input().split(' '))
#    for j in range(Dorm):
#        student.append(int(input()))
#        cnt_student += student[j]
#        AP_Dorm.append(int(1))
#    AP -= Dorm
#    while True:
#        a = student.index(max(student))
#        AP_Dorm[a] += 1
#        student[a] = (student[a] * (AP_Dorm[a] - 1)) / (AP_Dorm[a])
#        AP -= 1
#        if (AP == 0):
#            break
#    student.sort(reverse = True)
#    if cnt_student <= AP:
#        print(1)
#        exit(1)
#    else: 
#        print(int(student[0]))

N = "A"
print(chr(65))
