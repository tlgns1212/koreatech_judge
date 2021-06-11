##성공
#N = int(input())
#min = input()
#for i in range(1,N):
#    use = input()
#    if len(min) > len(use):
#        min = use
#print(min)



#재용이꺼
#q = []
#q.append(input('문자열 입력하시오: '))
#a = q.pop()
#print(a)


#상현이꺼
def count(self,str):
    self.c= 0
    for i in range(0,len(str)):
        if str[i] in "1234567890":
            return False
        else: c+=1
    return c