import time;
import datetime;
print ''
print ''
print ''
print ''
print 'Taking u all to the era of 70s'
print '|*****************************|'
print '*'
print '*'
print '*'
print '*'
print '*'
print 'Moon Techs'
print 'Welcomes you to the Future!'
print '*'
print '*'
print '*'
print '*'
print '*'
print '*'
print '|*****************************|'
print ''
print ''
print 'Featuring the most advanced A.I spy of our time!'
print 'Heyy'
gender=raw_input('Male or Female:')
if(gender=='Male'or'm'or'male'or'MALE'or'M'):
    name=raw_input("Enter your name:")
    print ''
    time.sleep(0.2)
    print 'I am a Spy'
    print 'Just for folks!!!'
    print ''
    print 'Welcome'
    print 'Mr./Ms.'+name
    age=int(raw_input('Enter you age:'))
    year = str(datetime.date.today().year-age)
    print 'So lemme guess...'
    time.sleep(1)
    print 'You were born in:',year


elif(gender=='Female'or'F'or'FEMALE'or'f'):
    name=raw_input("Enter your name:")
    print ''
    time.sleep(0.2)
    print 'I am a Spy'
    print 'Just for folks!!!'
    print ''
    print 'Welcome'
    print 'Mrs./Miss.'+name
    age=int(raw_input('Enter you age:'))
    year = str(datetime.date.today().year-age)
    print 'So lemme guess...'
    time.sleep(1)
    print 'You were born in:',year

