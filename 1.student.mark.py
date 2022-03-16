slist = []
scourse = dict()
def std_info():
    std_total = int(input('Enter number of student:'))
    for i in range (std_total):
        s_info = {}
        s_info['name'] = input('enter name')
        s_info['id'] = input('enter id')
        s_info['mark'] = input('enter mark')
        s_info['courses'] = int(input('enter number of courses:'))
        slist.append(s_info)  
std_info()
print(slist)


