hours=input('Enter hours: ')
rate=input('Enter rate: ')
try:
    h=float(hours)
    r=float(rate)
except:
    print('Error, please enter numeric input')
    quit()
if h<=40:
    pay=h*r
if h>40:
    pay=(40*r)+((h-40)*(r*1.5))
print(pay)