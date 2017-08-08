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
if ((gender.upper()=='MALE') or (gender.upper()=='M')):
    name=raw_input("Enter your name:")
    print ''
    time.sleep(0.5)
    print 'I am a Spy'
    print 'Just for folks!!!'
    print ''
    print 'Welcome'
    marital=raw_input('Married or not? \n')
    if marital=='Yes':
        salutation='Mr.'
        print salutation+name
    else:
        salutation='Mr.'
        print salutation+name
    print 'Alright,I would liketo know a little more about you...'
    age=raw_input('Enter you age:')

    while(age.isalpha()):
        print 'Enter a numeric value'
        age=int(raw_input('Enter your age:'))


    year = str(datetime.date.today().year-age)
    print 'So lemme guess...'
    time.sleep(1)
    print 'You were born in:',year
    if age<100:
        old=100+int(year)
        print 'You will be 100 years old in:',old
    else:
        old=100+int(year)
        print 'You were 100 years older in:',old

elif ((gender.upper()=='FEMALE') or (gender.upper()=='F')):
    name=raw_input("Enter your name:")
    print ''
    time.sleep(0.5)
    print 'I am a Spy'
    print 'Just for folks!!!'
    print ''
    print 'Welcome'
    marital=raw_input('Married or not ? \n')
    if ((marital.upper()=='YES') or (marital.upper()=='MARRIED')or(marital.upper()=='NOT')):
        salutation='Mrs.'
        print salutation+name
    else:
        salutation='Ms.'
        print salutation + name
    age=int(raw_input('Enter you age:'))
    year = str(datetime.date.today().year-age)
    print 'So lemme guess...'
    time.sleep(1)
    if age<100:
        old=100+int(year)
        print 'You will be 100 years old in:',old
    else:
        old=100+int(year)
        print 'You were 100 years older in:',old
else:
    print 'I do not think you have gender.'