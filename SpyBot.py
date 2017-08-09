from Spy_Alpha import spy_name,spy_age,spy_rating
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
    if marital=='Married':
        salutation='Mr.'
        print salutation+name
    else:
        marital = 'Not Married'
        salutation='Mr.'
        print salutation+name
    print '\n Alright,I would like to know a little more about you...'
    age=raw_input('Enter you age:')

    while(age.isalpha()):
        print 'Enter a numeric value'
        age=(raw_input('Enter your age:'))

    year = datetime.date.today().year-int(age)
    print 'So lemme guess...'
    time.sleep(1)
    print 'You were born in:',year
    age=int(age)
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
    if ((marital.upper()=='YES') or (marital.upper()=='MARRIED')):
        salutation='Mrs.'
        print salutation+name
    else:
        salutation='Miss.'
        marital='Not Married'
        print salutation + name
    print '\n Alright,I would like to know a little more about you...'
    age = raw_input('Enter you age:')

    while (age.isalpha()):
        print 'Enter a numeric value'
        age = (raw_input('Enter your age:'))

    year = datetime.date.today().year - int(age)
    print 'So lemme guess...'
    time.sleep(1)
    print 'You were born in:', year
    age=int(age)
    if age < 100:
        old = 100 + int(year)
        print 'You will be 100 years old in:', old
    else:
        old = 100 + int(year)
        print 'You were 100 years older in:', old

else:
    print 'Sorry! I can\'t help you out...'

time.sleep(1)
status='Not updated yet!'
def start_chat(spy_name,spy_age,spy_rating):
    global status
    show_menu=True
    while show_menu:
        print '\n'
        print 'Select any of the following:'
        choices='1.Add a status update \n2.Add a friend \n3.Send a secret message \n4.Read a secret message \n5.Read Chats from user \n6.Show your profile \n7.Terminate \n\n'
        ch=int(raw_input(choices))
        if ch==1:
            print 'Time to update the status!'
            status=raw_input('Enter your status:')
            print 'Updated Status:',status
        elif ch==2:
            print 'Under Development'
        elif ch==3:
            print 'Under Development'
        elif ch==4:
            print 'Under Development'
        elif ch==5:
            print 'Under Development'
        elif ch==6:
            print ''
            print 'Your Profile:'
            print 'Name:',salutation+name
            print 'Age:',age
            print 'Marital Status:',marital
            print 'Status: \n',status
        elif ch==7:
            show_menu =False
            print 'Terminating...'
            time.sleep(0.7)
            print 'Eventually Terminated'

start_chat(spy_name,spy_age,spy_rating)