#coding=utf-8
try:
    #print(a[2])
    print('this is normal')
except Exception as e:
	#raise
    print(u'except')
else:
    print('this is not except')
finally:
    print(u'no way i must be ctrl')