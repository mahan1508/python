#ticket
gender=input('gender>> ')
age=int(input('age =  '))
if gender=='female':
    print('ticket free')
else:
    if age<5:
        print('ticket  free')
    elif age<=15:
        print('half ticket')
    elif age>=15:
        print('full ticket')
    else:
        print('you need to pay the full ticket')
'''
#signal
signal=input('signal=  ')
if signal=='red':
    print('stop')
elif signal=='yellow':
    print('ready')
elif signal=='green':
    print('goooo')
else:
    print('invalid signal colour')
'''
'''                 
#attendence
att=int(input('enter the attendence of the student>> '))
is_student_friend=True
if att<=75 or is_student_friend:
    print('give exam')
else:
    print("no exam will be givven") '''   
